from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
  class Types(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"

  type = models.CharField(max_length=20, choices=Types.choices, default=Types.USER)

  usersname = models.CharField(max_length=255, null=False, unique=True) #text fields with max characters
  email = models.EmailField(null=False, unique=True)
  password = models.CharField(max_length=255, null=False)

  def __str__(self):
    return self.username
  
