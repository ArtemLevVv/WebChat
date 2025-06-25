from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
# Create your views here.

class ViewChats(TemplateView):
    template_name = 'chats/chats.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.is_anonymous:
            return redirect('sign_up')
        return super().dispatch(request, *args, **kwargs)