from django.shortcuts import render

from catalogue.models import Fruit

# Create your views here.
def login_page(request):
  return render(request, "login.html")

def admin_page(request):
  fruits = Fruit.objects.all()
  return render(request, "admin.html", {
    "fruits": fruits
  })