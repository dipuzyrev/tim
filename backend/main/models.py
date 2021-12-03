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


class Project(models.Model):
    """
    Main project model
    """

    title = models.TextField()
    description = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)

    PILOT_CHOICES = [
        ('1', 'Нет'),
        ('2', 'В прогрессе'),
        ('3', 'Пройден'),
    ]
    pilot = models.CharField(
        max_length=1,
        choices=PILOT_CHOICES,
        default='1',
    )

    success_pilot = models.BooleanField(null=True)
    tags = models.JSONField(null=True, blank=True)
    thumbnail = models.TextField(null=True, blank=True)
    product_stage = models.TextField(null=True, blank=True)
    requires_cert = models.BooleanField(default=False)
    team_size = models.PositiveIntegerField()

    ORGANISATION_CHOICES = [
        ('1', 'Московский метрополитен'),
        ('2', 'Мосгорстранс'),
        ('3', 'ЦОДД'),
        ('4', 'Организатор перевозок'),
        ('5', 'Мостранспроект'),
        ('6', 'АМПП'),
    ]
    prior_organization = models.CharField(
        max_length=1,
        choices=ORGANISATION_CHOICES,
        default='1',
    )

    use_cases = models.TextField(null=True, blank=True)
    presentation_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class CustomProjectRequest(models.Model):
    """
    Requests for specific project from transport company
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pain = models.TextField(null=True, blank=True)
    problem = models.TextField(null=True, blank=True)
    what_if = models.TextField(null=True, blank=True)
    why = models.TextField(null=True, blank=True)
    whose_pain = models.TextField(null=True, blank=True)
    period = models.TextField(null=True, blank=True)
    tried = models.TextField(null=True, blank=True)
    contacts = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.pain}'


class SelectProjectRequest(models.Model):
    """
    Selected projects
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='selected_project')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.project}'

