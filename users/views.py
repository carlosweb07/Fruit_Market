from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
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
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user = authenticate(request, email=email, password=password)  
        print(user)
        if user is not None:
            login(request, user)  
            print('listo')
            return redirect('/home') 
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