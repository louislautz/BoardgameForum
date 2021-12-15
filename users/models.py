from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("Every user must have a username")
        if not password:
            raise ValueError("Every user must have a password")

        user = self.model(username = username)
        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.save()
        return user

    def create_staffuser(self, username, password=None):
        user = self.create_user(
                username,
                password = password,
                is_staff = True)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
                username,
                password = password,
                is_staff = True,
                is_admin = True)
        return user


class User(AbstractBaseUser):
    """Extends pre-built User model"""
    username = models.CharField(max_length=50, unique=True)
    biography = models.CharField(max_length=300)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()  # Links this extended user class to its manager

    def __str__(self):
        """Returns a string that describes the user"""
        return self.username

    # Django built-in function we need to create manually now, because
    # we are not using the vanilla User model

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
