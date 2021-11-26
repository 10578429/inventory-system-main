from django.db import models

from inventory.models import Product


# Create your models here.
class Cart(models.Model):

    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveSmallIntegerField(default=1)
    total = models.DecimalField(decimal_places=2, max_digits=100000)

