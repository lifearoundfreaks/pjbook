from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile


class CreateUserForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2']
