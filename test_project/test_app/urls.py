from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('become_orderer', views.become_orderer, name='become_orderer'),
    path('become_executor', views.become_executor, name='become_executor'),
    path('set_experience', views.set_experience, name='set_experience'),
    path('profile/', views.profile, name='profile'),
    path('profile/executor', views.profile_executor, name='profile-executor'),
    path('admin/', views.admin_redirect, name='admin')
]
