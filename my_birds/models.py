from django.db import models

# Create your models here.

# models.py
from django.db import models

class Bird(models.Model):
    common_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    
    def __str__(self):
      return self.common_name