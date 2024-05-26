from django.db import models
# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
    City = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    Phone = models.CharField(max_length=11)

 