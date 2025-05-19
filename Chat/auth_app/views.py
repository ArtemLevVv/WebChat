from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
# Create your views here.


class ViewLogin(TemplateView):
    template_name = 'login/login.html'

class ViewSignup(TemplateView):
    template_name = 'signup/signup.html'