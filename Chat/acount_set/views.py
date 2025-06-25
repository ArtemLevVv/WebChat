from django.shortcuts import render
from django.shortcuts import redirect
from .forms import AlbumForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

# def redirect_view(request):
#     return redirect('signup')

class ViewAcountSet(TemplateView):
    template_name = 'acount_set/acount_set.html'

class ViewAlbom(CreateView):
    template_name = 'alboms/alboms.html'
    form_class = AlbumForm
    success_url = reverse_lazy("home_app")

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     if request.user.is_anonymous:
    #         return redirect('sign_up')
    #     return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        return super().form_valid(form)

    # def Add_Album(request):
    #     if request.method == 'POST':
    #         form = AlbumForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('album_list')
    #     else:
    #         form = AlbumForm()
    #     return render(request, 'alboms.html', {'form': form}) 

