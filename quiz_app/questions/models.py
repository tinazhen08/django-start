from django.db import models

class Users(models.Model):
  firstname = models.CharField(max_length=255) #text firlds with max characters
  lastname = models.CharField(max_length=255)

  