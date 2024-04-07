from django.shortcuts import render

# esta lista es temporal tranquilos XD
fruits = [
  {
    "id": 1,
    "name": "Manzana",
    "category": "Dulce",
    "available_units": 20,
    "price": 2,
    "img": "catalogue/static/imgs/manzana.png"
  },
  {
    "id": 2,
    "name": "Fresa",
    "category": "Semiacida",
    "available_units": 50,
    "price": 4,
    "img": "catalogue/static/imgs/fresa.png"
  },
  {
    "id": 3,
    "name": "Aguacate",
    "category": "Neutral",
    "available_units": 100,
    "price": 6,
    "img": "catalogue/static/imgs/aguacate.png"
  },
  {
    "id": 4,
    "name": "Patilla",
    "category": "Dulce",
    "available_units": 20,
    "price": 10,
    "img": "catalogue/static/imgs/sandia.png"
  },
]

def home_page(request):
  return render(request, "index.html")

def catalogue_page(request):
  return render(request, "catalogue.html", {
    "fruits": fruits
  })

def fruit_page(request, id):
  return render(request, "fruit.html", {
    "fruit": fruits[id - 1]
  })