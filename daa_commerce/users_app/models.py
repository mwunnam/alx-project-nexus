from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstracUser):
    email = model.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

