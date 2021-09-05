from django.db import models
from login.models import User

class Mensaje(models.Model):
    usuario = models.ForeignKey(User, related_name='mensajes', on_delete= models.CASCADE)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Usuario: {self.usuario}\nMensaje: {self.mensaje}\n'
    def __str__(self):
        return f'Usuario: {self.usuario}\nMensaje: {self.mensaje}\n'

class Comentario(models.Model):
    usuario = models.ForeignKey(User, related_name='comentarios_user', on_delete= models.CASCADE)
    mensaje = models.ForeignKey(Mensaje, related_name='comentarios_mensaje', on_delete= models.CASCADE)
    comentario = models.TextField(default='Mensaje Vacio')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Usuario: {self.usuario}\nMensaje: {self.mensaje}\nComentario: {self.comentario}'
    def __str__(self):
        return f'Usuario: {self.usuario}\nMensaje: {self.mensaje}\nComentario: {self.comentario}'
