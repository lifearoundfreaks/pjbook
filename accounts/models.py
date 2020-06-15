from django.contrib.auth.models import User
from django.db import models


class UserProfile(User):

    notes = models.CharField(max_length=255)
