from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.register_view, name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('auth/logout/', views.logout_view, name='logout')
]
