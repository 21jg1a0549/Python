from django.db import models

class UserDetails(models.Model):
    userid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone= models.IntegerField()
    address = models.TextField()
    password = models.CharField(max_length=128)
    objects = models.Manager()  # Note: You missed the parentheses here



