from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapp/', include('userapp.urls')),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/password_change_form/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),  
    path('accounts/password_change_form/', user_views.change, name='password_change'),
    path('', RedirectView.as_view(url='/userapp/')),
    
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



