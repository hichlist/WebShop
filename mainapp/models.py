from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
#    quantity = models.IntegerField()