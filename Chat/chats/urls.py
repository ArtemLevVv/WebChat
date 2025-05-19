from django.urls import path, include 
from .views import ViewChats

urlpatterns = [
    path('chats/', view = ViewChats.as_view(), name='chats')
]