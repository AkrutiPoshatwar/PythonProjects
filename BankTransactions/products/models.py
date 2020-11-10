from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=50)
    total_sale = models.IntegerField(default=0)