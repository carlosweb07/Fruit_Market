from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from jinja2 import Environment, FileSystemLoader
from catalogue.models import Fruit, Category

import pdfkit

# Create your views here.
@login_required
def admin_page(request):
  fruits = Fruit.objects.all()
  return render(request, "admin.html", {
    "fruits": fruits
  })

def login_page(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)  
            print('listo')
            return redirect('/catalogue') 
        else: 
            return render(request, "login.html", {'error': 'Correo o clave invalida'})

def register_page(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:  
      try:
          user = User.objects.create_user(
            request.POST["username"],
            request.POST["email"],
            request.POST["password"],
          )
          user.save()
          login(request, user)
          return redirect('/login') 
      except:
        return render(request, "register.html", {
            "error": "El usuario ya existe"
        })
      
def signout(request):
  logout(request)
  return redirect("/")

def create_page(request):
  if request.method == "GET":
      categories = Category.objects.all()
      return render(request, "create.html", {
        "categories": categories
      })
  else:
      category = Category.objects.get(id=request.POST["category"])
      
      fruit = Fruit()
      
      fruit.name = request.POST["name"]
      fruit.img = request.FILES["img"]
      fruit.category = category
      fruit.available_units = request.POST["available_units"]
      fruit.price = request.POST["price"]
      
      fruit.save()
      return redirect("/admin")

def edit_page(request, id):
    if request.method == "GET":
      fruit = Fruit.objects.get(id=id)
      categories = Category.objects.all()
      return render(request, "edit.html", {
        "fruit": fruit,
        "categories": categories
      })
    else:
      fruit = Fruit.objects.get(id=id)
      category = Category.objects.get(id=request.POST["category"])
      
      fruit.name = request.POST["name"]
      fruit.img = request.FILES["img"]
      fruit.category = category
      fruit.available_units = request.POST["available_units"]
      fruit.price = request.POST["price"]
      fruit.save()
      
      return redirect("/admin")
    
def delete(request, id):
   fruit = Fruit.objects.get(id=id)
   fruit.delete()

   return redirect("/admin")

def gestor_page(request):
  return render(request, "gestor.html")

def export_fruits(request):
  fruits = Fruit.objects.all()
  
  config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
  
  env = Environment(loader=FileSystemLoader("users/templates/reports"))
  template = env.get_template("pdf_frutas.html")
  
  html = template.render({
    "fruits": fruits
  })
  
  pdfkit.from_string(
    html,
    "report_fruits.pdf",
    options={"enable-local-file-access": ""},
    configuration=config
  )
  
  return redirect("/gestor")

def export_users(request):
  users = User.objects.all()
  
  config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
  
  env = Environment(loader=FileSystemLoader("users/templates/reports"))
  template = env.get_template("pdf_usuarios.html")
  
  html = template.render({
    "users": users
  })
  
  pdfkit.from_string(
    html,
    "report_users.pdf",
    options={"enable-local-file-access": ""},
    configuration=config
  )
  
  return redirect("/gestor")