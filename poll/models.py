from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

class poll(models.Model):
    name = models.CharField(max_length=100)  # Max length of 100 characters
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    Homepage_des=HTMLField()
    Overall_des=HTMLField()
    Exterior_des=HTMLField()
    Interior_des=HTMLField()
    main_img = models.ImageField(upload_to='images/', null=True, blank=True)
    Exterior_img1 = models.ImageField(upload_to='images/', null=True, blank=True)
    Exterior_img2 = models.ImageField(upload_to='images/', null=True, blank=True)
    interior_img1 = models.ImageField(upload_to='images/', null=True, blank=True)
    interior_img2 = models.ImageField(upload_to='images/', null=True, blank=True)
    count = models.IntegerField(default=0)
    slugs=AutoSlugField(populate_from='name', unique=True , null=True , default=None)
    
    

    

   

