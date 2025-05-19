from .views import ViewLogin, ViewSignup
from django.urls import path, include

urlpatterns = [
    path('login/',view = ViewLogin.as_view(), name='login'),
    path('signup/', view = ViewSignup.as_view(), name='signup')

]