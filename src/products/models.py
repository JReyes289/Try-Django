from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description =models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=100)
    summary = models.CharField(max_length=200,default="this is a tutorial")
    feature = models.BooleanField(default=False)