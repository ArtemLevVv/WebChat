from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.http import HttpRequest
# Create your views here.



class ViewHome(TemplateView):
    template_name = 'home_app/home_app.html'
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     if request.user.is_anonymous:
    #         return redirect('sign_up')
    #     return super().dispatch(request, *args, **kwargs)     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        
        user = self.request.user
        
        context['show_modal'] = not user.email if user.is_authenticated else False
        context['show_profile'] = True
        return context
    

    

