from django.urls import path, include

from .views import ViewPublication, ViewFormPublication, ViewDeletePost, ViewEditPost

urlpatterns = [
    path(route= 'publication/', view=ViewPublication.as_view(), name='my_publication'),
    path(route= 'publication/<int:pk>/delete', view = ViewDeletePost.as_view(), name= 'delete_post'),
    path(route= 'publication/<int:pk>/edit', view= ViewEditPost.as_view(), name= 'edit_post'),
    path(route= 'publication_form/', view= ViewFormPublication.as_view(), name= 'publication_form'),
]