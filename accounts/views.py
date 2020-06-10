from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import FormView
from accounts.forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login


class SignInView(AccessMixin, LoginView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignOutView(LoginRequiredMixin, LogoutView):
    next_page = 'popular_projects'


class RegistrationView(AccessMixin, FormView):
    form_class = CreateUserForm
    template_name = "accounts/registration.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('popular_projects')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect(self.get_success_url())

        return render(request, self.template_name, {'form': form})
