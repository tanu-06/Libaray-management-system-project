from django.db import models
# Create your models here.

class User(models.Model):
   refid = models.IntegerField()
   bookname = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   language = models.CharField(max_length=100)

