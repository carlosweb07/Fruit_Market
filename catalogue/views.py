from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Fruit

def home_page(request):
  return render(request, "index.html")

@login_required
def catalogue_page(request):
  fruits = Fruit.objects.all()
  return render(request, "catalogue.html", {
    "fruits": fruits
  })

@login_required
def fruit_page(request, id):
  fruit = Fruit.objects.get(id=id)
  return render(request, "fruit.html", {
    "fruit": fruit
  })