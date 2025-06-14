from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from .forms import ModalFormExtraInfo
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from my_publication.models import UserPostModel

# Create your views here.

# get_user_model відповідає за отримання моделі

class ViewHome(FormView):
    template_name = 'home_app/home_app.html'
    form_class = ModalFormExtraInfo
    success_url = reverse_lazy('home_app')
    # якщо форма валдіна то тоді ми виконуємо запис диних
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        user = self.request.user
        t_f_show = False
        print(user.is_authenticated)
        print(self.request.user.username)
        if user.is_authenticated and not self.request.user.email:
            t_f_show = True

        context['posts'] = UserPostModel.objects.order_by('-id')
        context['form'] = self.form_class()
        context['show_modal'] = t_f_show
        context['show_profile'] = True
        context['username'] = self.request.user.username
        return context
    
    def form_valid(self, form):
        user = self.request.user

        new_login = form.cleaned_data['login']

        if User.objects.filter(username=new_login).exclude(pk=user.pk).exists():
            form.add_error('login', 'Цей логін уже зайнятий іншим користувачем.')
            return self.form_invalid(form)

        user.email = user.username 
        user.username = new_login

        print(user.email)
        user.first_name = form.cleaned_data['username']
        user.last_name = form.cleaned_data['last_name']

        user.save()
        return super().form_valid(form)
    
    # передає зміни в форму
    def get_form_kwargs(self):
        # бере стандартні аргументи
        kwargs = super().get_form_kwargs()
        # додає початкові значення які автоматино підставляє в форму
        kwargs['initial'] = {
            'username' : self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'login': self.request.user.username,
        }
        return kwargs