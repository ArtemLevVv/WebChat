from django.urls import path, include 
from .views import ViewAcountSet, ViewAlbom
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('acountSettings/', view = ViewAcountSet.as_view(), name="acount_set"),
    path('alboms/', view= ViewAlbom.as_view(), name="alboms"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)