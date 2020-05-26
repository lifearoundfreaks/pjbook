from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import SignInForm, CreateUserForm


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class SignOutView(LogoutView):
    next_page = '/'


def registration(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    return render(request, 'accounts/registration.html', context)
