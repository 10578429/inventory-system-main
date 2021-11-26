from django.db import models


# Create your models here.
class Product(models.Model):

    class ProductCategories(models.TextChoices):
        NONE = ('', 'Please Select')
        MEAT_AND_FISH = ('MF', 'Meat and Fish')
        VEGETABLES = ('VEG', 'Fruit and Vegetables')

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(choices=ProductCategories.choices, max_length=5, default=ProductCategories.NONE)
    image = models.ImageField(upload_to='images/', max_length=1000)
    available = models.BooleanField()
