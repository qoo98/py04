from django.shortcuts import render, redirect
from django.contrib import messages
# Import User UpdateForm, ProfileUpdatForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserNameUpdateForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm, UserChangeForm, ChangePasswordForm, ConfirmPasswordForm
)
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login
from django.urls import reverse
from userapp.models import Shop
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            post = form.save() 
            email = form.cleaned_data.get('email') 
            post.username = email.split('@')[0]
            post.save()  
            username = post.username
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('userapp:index')
            else:
                return HttpResponse('ユーザーが存在しません')

        return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Update it here
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserNameUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) 
        c_form = ConfirmPasswordForm(user_id=request.user.id, data=request.POST)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')

            return redirect('profile') 


    else:
        u_form = UserNameUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        c_form = ConfirmPasswordForm(user_id=request.user.id)


    context = {
        'shops': Shop.objects.all(),
        'u_form': u_form,
        'p_form': p_form,
        'c_form': c_form,
    }

    return render(request, 'users/profile.html', context)


def change(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        pass_form = ChangePasswordForm(user_id=request.user.id, data=request.POST)
        email_form = UserUpdateForm(request.POST, instance=request.user)
        if pass_form.is_valid() and email_form.is_valid():
            new_password = pass_form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            email_form.save()
            user = authenticate(
                username=user.username,
                password=new_password,)
            if user is not None:
                login(request, user)

            return redirect('userapp:index')

    else:
        pass_form = ChangePasswordForm(user_id=request.user.id)
        email_form = UserUpdateForm(instance=request.user)



    context = {
        'pass_form': pass_form,
        'email_form': email_form,
    }

    return render(request, 'registration/password_change.html', context)


class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}


class ConfirmView(SuccessURLAllowedHostsMixin, FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = ConfirmPasswordForm

