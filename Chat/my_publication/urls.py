from django.urls import path, include

from .views import ViewPublication

urlpatterns = [
    path('publication/', view=ViewPublication.as_view(), name='my_publication')
]