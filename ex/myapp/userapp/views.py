from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import Shop
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import sys
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'shop_list.html'
    model = Shop


class DetailView(generic.DetailView):
    template_name = 'userapp/show_detail.html'
    model = Shop
    


    def get_context_data(self, *args, **kwargs):
        indexshop = Shop.objects.get(pk=self.kwargs['pk'])
        ctx = super().get_context_data()
        ctx['shops'] = Shop.objects.filter(address=indexshop.address)
        return ctx




class CreateView(generic.edit.CreateView):
    model = Shop
    fields = ['name', 'address', 'message']
                   
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].label = 'title'
        form.fields['address'].label = 'URL'
        form.fields['message'].label = 'comment'
        return form

    def post(self, request, *args, **kwargs):
        author = self.request.user
        name=request.POST['name']
        address=request.POST['address']
        message=request.POST['message']
        user_content = Shop(author=author, name=name, address=address, message=message)
        user_content.save()
        return redirect('userapp:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)





# class ProfileView(generic.edit.CreateView):
class ProfileView(generic.TemplateView):

    template_name = 'userapp/profile.html'
    fields = ['username']
    model = Shop

    def save(self, request, *args, **kwargs):
        author = self.request.user
        username = author.username.split('@')[0]
        user_content = Shop(author=author, username=username)
        user_content.save()        

    def get_success_url(self):
        return reverse('userapp:profile')

class UpdateView(generic.edit.UpdateView):
    fields = ['name']


    # class //View(LoginRequireMixin, generic.edit.//View)

class DeleteView(generic.edit.DeleteView): 
    model = User
    success_url = reverse_lazy('userapp:deleted')

class DeletedView(generic.TemplateView):
    template_name = 'userapp/deleted.html'

    def get_success_url(self):
        return reverse('userapp:deleted')
