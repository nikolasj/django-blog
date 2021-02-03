from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
# from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField('username', max_length=150, blank=True)
    email = models.EmailField('email address', blank=False, unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
