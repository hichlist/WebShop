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
#   Выводит имя товара в админке

    def __str__(self):
        return self.name


class Contact(models.Model):
    sender = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
