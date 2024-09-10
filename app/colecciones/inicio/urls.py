from django.urls import path
from django.contrib.auth import views as views_auth
from app.inicio.views import *

urlpatterns = [

    path('login/', views_auth.LoginView.as_view(template_name = 'inicio/login.html'), name = 'login'),
    path('logout/', views_auth.LogoutView.as_view(template_name = 'inicio/login.html'), name = 'logout'),
    path('', Home.as_view(), name = 'home'),
    
]