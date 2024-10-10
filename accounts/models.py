# SPDX-License-Identifier: Apache-2.0 #

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, terms_accepted, **extra_fields):
        if not email:
            raise ValueError(_("error_message_missing_email"))
        email = self.normalize_email(email)
        print('create user')
        print(terms_accepted)
        print(str(extra_fields))
        if extra_fields.get("is_superuser"):
            user = self.model(first_name="admin", email=email, **extra_fields)
        else:
            user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    username = None
    first_name = models.CharField(max_length=128, blank=False, null=False)
    terms_accepted = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
