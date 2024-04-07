from django.db import models

# Create your models here.
class acidas(models.acidas):
    name = models.CharField(max_length=255)
    category = models.ForeignKey()
    avaible_units = models.FloatField(max_length=50)
    price = models.FloatField(max_length=500)
    img = models.ImageField(upload_to='DIRECION')

    def __str__(self):
        return f"{self.name} {self.category} {self.avaible_units} {self.price} {self.img}"
    
class semiacidas(models.semiacidas):
    name = models.CharField(max_length=255)
    category = models.ForeignKey()
    avaible_units = models.FloatField(max_length=50)
    price = models.FloatField(max_length=500)
    img = models.ImageField(upload_to='DIRECION')

    def __str__(self):
        return f"{self.name} {self.category} {self.avaible_units} {self.price} {self.img}"
    
class neutro(models.neutro):
    name = models.CharField(max_length=255)
    category = models.ForeignKey()
    avaible_units = models.FloatField(max_length=50)
    price = models.FloatField(max_length=500)
    img = models.ImageField(upload_to='DIRECION')

    def __str__(self):
        return f"{self.name} {self.category} {self.avaible_units} {self.price} {self.img}"
    
class dulces(models.dulces):
    name = models.CharField(max_length=255)
    category = models.ForeignKey()
    avaible_units = models.FloatField(max_length=50)
    price = models.FloatField(max_length=500)
    img = models.ImageField(upload_to='DIRECION')

    def __str__(self):
        return f"{self.name} {self.category} {self.avaible_units} {self.price} {self.img}"
