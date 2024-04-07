from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    avaible_units = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    img = models.ImageField(upload_to='catalogue/static/imgs')

    def __str__(self):
        return f"{self.name} {self.category} {self.avaible_units} {self.price} {self.img}"
    