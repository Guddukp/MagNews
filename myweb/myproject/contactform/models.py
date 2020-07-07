from __future__ import unicode_literals
from django.db import models

# Create your models here.

class ContactForm(models.Model):
     
     cname = models.CharField(max_length=50)
     cemail = models.CharField(max_length=50)
     ctxt = models.TextField()
     
     def __str__(self):
        return self.name  

    
