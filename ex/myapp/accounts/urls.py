from django.urls import path
from . import views

from accounts.forms import EmailAuthenticationForm
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
       path('login/', LoginView.as_view(
    form_class=EmailAuthenticationForm,
    redirect_authenticated_user=True,
    template_name='users/login.html'
), name='login'),
]