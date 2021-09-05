from django.shortcuts import render , redirect
from .models import *

def wall(request):
    if 'usuario' not in request.session:
        return redirect('/')
    else:
        mensajes = Mensaje.objects.all().order_by('-created_at')
        contexto = {
            'mensajes' : mensajes,
        }
        # print(request.POST)
        return render(request ,'wall.html' , contexto)

def crearMensaje(request , id):
    usuario = User.objects.get(id = id)
    mensaje = Mensaje.objects.create(
        usuario = usuario,
        mensaje = request.POST['mensaje'],
    )
    # print(request.POST)
    return redirect('/wall')