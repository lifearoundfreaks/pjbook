from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import FormView, DetailView
from accounts.forms import CreateUserForm
from accounts.models import UserProfile


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'

    def get_success_url(self):
        return reverse('popular_projects')


class SignOutView(LogoutView):
    next_page = '/'


class RegistrationView(FormView):
    form_class = CreateUserForm
    template_name = "accounts/registration.html"

    def get_success_url(self):
        return reverse('sign_in')

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationView, self).form_invalid(form)


class ProfileView(DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'
