from django.urls import path, include 
from .views import ViewAcountSet

urlpatterns = [
    path('acountSettings/', view = ViewAcountSet.as_view(), name="acount_set")
]