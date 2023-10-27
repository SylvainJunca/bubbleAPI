from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from apps.shared.models import UUIDModel, TimestampModel
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, UUIDModel, TimestampModel):
    email = models.EmailField('email', unique=True)
    username = models.CharField(
        'username',
        max_length=32,
        validators=[MinLengthValidator(3), MaxLengthValidator(32)],
        null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('username'),
                name='username_unique'
            ),
        ]
