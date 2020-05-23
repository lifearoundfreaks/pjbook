from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignInForm(AuthenticationForm):
    username = UsernameField(
        label=("Логин"), widget=forms.TextInput(attrs={'autofocus': True, 'class': 'span4', 'id': 'username'})
    )
    password = forms.CharField(
        label=("Пароль"), strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'span4', 'id': 'password'}),
    )

    error_messages = {
        'invalid_login': (
            "Пожалуйста, введите правильное имя пользователя и пароль."
        ),
        'inactive': ("Этот аккаунт не активен.")
    }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = []