from django.db import models

# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=15)
    phno=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=400)
    duration=models.IntegerField()
    fee=models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=100)
    phno=models.CharField(max_length=10)