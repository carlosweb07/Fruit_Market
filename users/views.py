from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from catalogue.models import Fruit

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