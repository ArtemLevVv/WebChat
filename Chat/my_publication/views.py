from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .forms import UserPostForm
# Create your views here.

class ViewPublication(TemplateView):
    template_name = 'my_publication/publication.html'
    form_post = UserPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_profile'] = True
        return context
    
class ViewFormPublication(TemplateView):
    template_name = 'form_publication/form_publication.html'
    form_post = UserPostForm

    # def 