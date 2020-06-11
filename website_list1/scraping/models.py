from django.db import models
from django.utils import timezone

class website_list(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
    
    class Admin:
        pass
