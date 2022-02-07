from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'userapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(template_name='userapp/deleted.html'), name='delete'),
    path('deleted/', views.DeletedView.as_view(), name='deleted'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
