from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    fields = ('username', 'password')
    success_url = reverse_lazy('worker_list')

