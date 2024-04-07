from django.shortcuts import render

from .models import Fruit
# esta lista es temporal tranquilos XD


def home_page(request):
  return render(request, "index.html")

def catalogue_page(request):
  fruits = Fruit.objects.all()
  return render(request, "catalogue.html", {
    "fruits": fruits
  })

def fruit_page(request, id):
  fruit = Fruit.objects.get(id=id)
  return render(request, "fruit.html", {
    "fruit": fruit
  })