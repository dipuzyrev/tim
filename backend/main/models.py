from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .managers import CustomUserManager


class User(AbstractUser):
    """
    Custom User model, use Email as username

    Default Django User fields, not stated here but existing:
    - password, first_name, last_name, date_joined, last_login
    - is_superuser, is_staff, is_active, user_permissions, groups
    """

    # Email and it's activation status and token
    email = models.EmailField(max_length=320, unique=True)
    USERNAME_FIELD = 'email'

    # Set username as non-required field
    username = models.CharField(max_length=1, blank=True, default='', help_text='Just skip this')

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

