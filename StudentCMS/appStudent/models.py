from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(max_length=11, null=False)
    name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=200, null=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)