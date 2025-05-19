from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
# Create your views here.

class ViewHome(TemplateView):
    template_name = 'home_app/home_app.html'
