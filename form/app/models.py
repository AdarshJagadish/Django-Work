from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.IntegerField()
    name=models.TextField()
    mark=models.IntegerField()