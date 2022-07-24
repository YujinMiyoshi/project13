from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .forms import LoginForm

class Top(TemplateView):
    template_name = 'todo/top.html'

class login(LoginView):
    form_class = LoginForm
    template_name = 'todo/login.html'

class Logout(LogoutView):
    template_name = 'todo/top.html'

# Create your views here.
