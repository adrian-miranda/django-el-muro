from django.db import models
from datetime import datetime
from datetime import date
import datetime
import re

class UserManager(models.Manager):
    def validacion(self, postData):
        errores={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        def edad_legal(date_birth):
            hoy = date.today()
            calculo_edad = hoy.year - date_birth.year - ((hoy.month, hoy.day) < (date_birth.month, date_birth.day))
            return  calculo_edad
        if len(postData['first_name']) < 2:
            errores['len_first_name'] = 'Nombre debe tener como minimo 2 caracteres'
        if len(postData['last_name']) < 2:
            errores['len_last_name'] = 'Apellido debe tener como minimo 2 caracteres'
        if not EMAIL_REGEX.match(postData['email']):      
            errores['email'] = "Correo Invalido"
        if len(postData['password']) < 8:
            errores['len_password'] = 'EL password debe tener a lo menos 8 caracteres'
        if len(postData['password_confirm']) < 8:
            errores['len_password_confirm'] = 'EL password debe tener a lo menos 8 caracteres'
        if (postData['password'] != postData['password_confirm']):
            errores['confirm'] = 'Las Contraseñas no coinciden'
        
        #validacion de edad
        hoyMismo = datetime.date.today()
        cumpleaños = datetime.datetime.strptime(postData['date_birth'], '%Y-%m-%d').date()
        if(cumpleaños > hoyMismo):
            errores['date_birth'] = 'La fecha de nacimiento no puede estar en el futuro'
        else:
            print(f'la edad es: {edad_legal}')
            if edad_legal(cumpleaños) < 16:
                errores['date_birth'] = 'Debes tener a lo menos 16 años para registrarte.'
        print(errores)
        return errores

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_birth = models.DateField()
    objects = UserManager() #este es el validador
    def __repr__(self):
        return f'nombre: {self.first_name}\napellido {self.last_name}\nemail: {self.email}\npassword: {self.password}\nfecha nacimiento {self.date_birth}'
    def __str__(self):
        return f'nombre: {self.first_name}\napellido {self.last_name}\nemail: {self.email}\npassword: {self.password}\nfecha nacimiento {self.date_birth}'