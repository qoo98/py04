from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='New Email')

    class Meta:
        model = User
        fields = ['email']


class UserNameUpdateForm(forms.ModelForm):
    username = forms.CharField(label='New Username')
    class Meta:
        model = User
        fields = ['username']

# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

