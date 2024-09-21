from django.db import models

# Create your models here.
class contactDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField(max_length=100,null=True,blank=True)

class registerDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)