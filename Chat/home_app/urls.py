from django.urls import path, include 
from .views import ViewHome

urlpatterns = [
    path('', view = ViewHome.as_view(), name='home_app')
]