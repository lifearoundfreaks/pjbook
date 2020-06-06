from django.urls import path
from .views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('sign_in/', LoginView.as_view(), name='sign_in'),
    path('sign_out/', LogoutView.as_view(), name='sign_out'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
