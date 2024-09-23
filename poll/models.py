from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

class poll(models.Model):
    name = models.CharField(max_length=100)  # Max length of 100 characters
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    dis1=HTMLField()
    dis2=HTMLField()
    img1 = models.ImageField(upload_to='images/', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', null=True, blank=True)
    count = models.IntegerField(default=0)
    slugs=AutoSlugField(populate_from='name', unique=True , null=True , default=None)
    
    

    

   

