from .views import ViewLogin, ViewSignup, CustomLogoutView, EmailCodeVerificationView
from django.urls import path, include

urlpatterns = [
    path('login/',view = ViewLogin.as_view(), name='login'),
    path('signup/', view = ViewSignup.as_view(), name='signup'),
    path('logout/', view = CustomLogoutView.as_view(), name='logout'),
    path('auth/verify-email/', view = EmailCodeVerificationView.as_view(), name='verify_email'),
]