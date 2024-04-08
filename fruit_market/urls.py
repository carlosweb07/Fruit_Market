"""
URL configuration for fruit_market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from catalogue import views as views_catalogue
from users import views as views_user

urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', views_catalogue.home_page),
    path('admin/', views_user.admin_page),
    path('create/', views_user.create_page),
    path('edit/<int:id>/', views_user.edit_page),
    path('catalogue/', views_catalogue.catalogue_page),
    path('fruit/<int:id>/', views_catalogue.fruit_page),
    path('login/', views_user.login_page),
    path('register/', views_user.register_page),
    path('logout/', views_user.signout),
]
