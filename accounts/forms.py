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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'span4'})
        self.fields['username'].label = 'Логин'
        self.fields['email'].widget.attrs.update({'class': 'span4'})
        self.fields['email'].label = 'Почта'
        self.fields['password1'].widget.attrs.update({'class': 'span4'})
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].widget.attrs.update({'class': 'span4'})
        self.fields['password2'].label = 'Пароль (повтор)'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
