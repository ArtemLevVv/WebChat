from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserPostForm
from .models import UserPostModel
# Create your views here.

class ViewPublication(TemplateView):
    template_name = 'my_publication/publication.html'
    form_post = UserPostForm

    def get_context_data(self, **kwargs):
        print(UserPostModel.objects.filter(user=self.request.user))
        context = super().get_context_data(**kwargs)
        context['show_profile'] = True
        context['username'] = self.request.user.username
        context['posts'] = UserPostModel.objects.filter(user=self.request.user).order_by('-id')
        return context
    
class ViewFormPublication(CreateView):
    template_name = 'form_publication/form_publication.html'
    form_class = UserPostForm
    success_url = reverse_lazy('home_app')
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # додати автора
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context