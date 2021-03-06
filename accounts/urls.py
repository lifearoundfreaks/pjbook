from django.urls import path
from .views import RegistrationView, SignInView, SignOutView

urlpatterns = [
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_out/', SignOutView.as_view(), name='sign_out'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
