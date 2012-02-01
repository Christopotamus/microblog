from django.db import models

# Create your models here.
class auth_users(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

class Author(models.Model):
    fullname = models.CharField(max_length=60)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    verif_number = models.CharField(max_length=16)
    verified = models.BooleanField()
    avatar_url = models.CharField(max_length=155)

class Wuphf(models.Model):
    author = models.ForeignKey(Author)
    text = models.CharField(max_length=140)
