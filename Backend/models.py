from django.db import models

# Create your models here.
class categoryDB(models.Model):
    category_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=100,null=True,blank=True)
    category_image=models.ImageField(upload_to="categories")

class productDB(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.IntegerField( null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    product_image = models.ImageField(upload_to="products")