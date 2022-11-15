from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):

    username = None
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # unique=True in URLField makes no sense (tested from admin panel)

    objects = UserManager()

    USERNAME_FIELD = "email"
    # should be included to avoid weird behaviour in admin panel, but not required
    # REQUIRED_FIELDS = ["full_name", "achievement_links", "background"]
    REQUIRED_FIELDS = []
