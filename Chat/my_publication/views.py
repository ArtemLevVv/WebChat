from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
# Create your views here.
class ViewPublication(TemplateView):
    template_name = 'my_publication/publication.html'