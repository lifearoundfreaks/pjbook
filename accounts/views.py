from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse

from accounts.forms import SignInForm


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class SignOutView(LogoutView):
    next_page = '/'
