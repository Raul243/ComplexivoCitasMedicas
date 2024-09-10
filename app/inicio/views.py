from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/home.html'
    login_url = 'inicio:login'
