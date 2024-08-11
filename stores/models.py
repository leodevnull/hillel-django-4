from django.db import models

from common.models import BaseModel
from products.models import Product


class Store(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='Inventory')


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
