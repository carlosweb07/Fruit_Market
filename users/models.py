from django.db import models

# Create your models here.

class register(models.user_register):
    correo = models.EmailField()
    password = models.PasswordField()
    password_second = models.PasswordField()


    def __str__(self):
        return {self.correo}, {self.password}, {self.password_second}

class login(models.user_login):
    correo = models.EmailField()
    password = models.PasswordField()

    def __str__(self):
        return {self.correo}, {self.password}
    