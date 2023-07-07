import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#AbstractBaseUser: Base class for creating user models. Can customizze fields according to needs
#PermissionsMixin : Gives ability to assign and manage permissions for user.
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password) #password is encrypted by this cmd
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #access to django admin to users is by default false

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retreive full name of user"""
        return self.name

    def get_full_name(self):
        """Retreive full name of user"""
        return self.name

    def __str__(self):
        return self.email