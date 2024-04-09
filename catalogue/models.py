from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

class Fruit(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available_units = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    img = models.ImageField(upload_to='catalogue/static/imgs')