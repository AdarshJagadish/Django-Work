from django.db import models

# Create your models here.
class teacher(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    
class media(models.Model):
    file=models.FileField()
    description=models.CharField(max_length=50)
