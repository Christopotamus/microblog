from django.db import models

# Create your models here.
class auth_users(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

class Author(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

class Wuphf(models.Model):
    author = models.ForeignKey(Author)
    text = models.CharField(max_length=140)
