from django.urls import reverse
from django.views.generic import FormView
from accounts.forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login


class RegistrationView(FormView):
    form_class = CreateUserForm
    template_name = "accounts/registration.html"

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect(self.get_success_url())

        return render(request, self.template_name, {'form': form})
