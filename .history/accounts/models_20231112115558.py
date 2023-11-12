from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
  def create_user(self, first_name, last_name, username, email, password=None):
    if not email:
      raise ValueError('User must have an email address')
    
    if not username:
      raise ValueError('User must have an username')
    
    user = self.model(
      email = self.normalize_email(email)
    )
  pass

class User(AbstractBaseUser):
  pass
