from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .forms import UserPostForm
# Create your views here.

# def redirect_view(request):
#     return redirect('signup')

class ViewPublication(TemplateView):
    template_name = 'my_publication/publication.html'
    form_post = UserPostForm
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     if request.user.is_anonymous:
    #         return redirect('sign_up')
    #     return super().dispatch(request, *args, **kwargs) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_profile'] = True
        return context
    
class ViewFormPublication(TemplateView):
    template_name = 'form_publication/form_publication.html'
    form_post = UserPostForm
