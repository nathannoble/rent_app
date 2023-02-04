from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']
