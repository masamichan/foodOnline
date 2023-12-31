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
      email = self.normalize_email(email),
      username = username,
      first_name = first_name,
      last_name = last_name
    )

    user.set_password(password)
    user.save(using = self._db)
    return user
  
  def create_superuser(self, first_name, last_name, username, email, password=None):
    user = self.create_user(
      email = self.normalize_email(email),
      username = username,
      first_name = first_name,
      last_name = last_name
    )
    user.is_admin = True
    user.is_active = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using = self._db)

    return user

  pass

class User(AbstractBaseUser):
  RESTAURANT = 1
  CUSTOMER = 2,

  ROLE_CHOICE = (
    (RESTAURANT, 'Restaurant'),
    (CUSTOMER, 'Customer')
  )
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  username = models.CharField(max_length = 50, unique=True)
  email = models.CharField(max_length = 100, unique=True)
  phone_number = models.CharField(max_length = 50)
  role = models.PositiveBigIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
  
  #required fields

  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now_add=True)
  created_date = models.DateTimeField(auto_now_add=True)
  modified_data = models.DateTimeField(auto_now_add=True)
  is_admin = models.DateTimeField(auto_now_add=True)
  is_staff = models.DateTimeField(auto_now_add=True)
  is_active = models.DateTimeField(auto_now_add=True)
  is_superadmin = models.DateTimeField(auto_now_add=True)

  USER_NAME = 'email'
  REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

  objects = 'email'

  def __str__(self):
    return self.email
  
  def has_perm(self, perm, obj=None):
    return self.is_admin
  
  def has_module_perms(self, app_label):
    return True
    
