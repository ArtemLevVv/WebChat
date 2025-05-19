from django.urls import path, include
from .views import ViewFriends

urlpatterns = [
    path('friends/', view = ViewFriends.as_view(), name='friends')
]