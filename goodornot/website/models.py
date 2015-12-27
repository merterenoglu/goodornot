
# Create your models here.
from __future__ import unicode_literals

from django.db import models




class Images(models.Model):
    
    idl = models.IntegerField()
    point = models.IntegerField()
    pic = models.ImageField(upload_to="images")

class Comments(models.Model):
    
    idl = models.IntegerField()
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=200)
  