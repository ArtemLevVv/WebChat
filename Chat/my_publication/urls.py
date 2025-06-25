from django.urls import path, include

from .views import ViewPublication, ViewFormPublication

urlpatterns = [
    path('publication/', view=ViewPublication.as_view(), name='my_publication'),
    path('publication_form/', view= ViewFormPublication.as_view(), name= 'publication_form'),
]