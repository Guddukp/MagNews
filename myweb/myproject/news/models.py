from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
 

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=150)
    short_txt = RichTextField()
    body_txt = RichTextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12,default="00:00")
    picname = models.TextField()
    picurl = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    catname = models.CharField(max_length=50,default="-")
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tag = models.TextField(default="")
     

    def __str__(self):

        return self.name

    
