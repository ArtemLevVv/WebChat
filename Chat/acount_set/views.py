from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
# Create your views here.

class ViewAcountSet(TemplateView):
    template_name = 'acount_set/acount_set.html'
