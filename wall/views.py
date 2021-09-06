from django.shortcuts import render , redirect
from .models import *

def wall(request):
    if 'usuario' not in request.session:
        return redirect('/')
    else:
        mensajes = Mensaje.objects.all().order_by('-created_at')
        comentarios = Comentario.objects.all()
        contexto = {
            'mensajes'      : mensajes,
            'comentarios'   : comentarios, 
        }
        return render(request , 'wall.html' , contexto)

def crearMensaje(request , id):
    usuario = User.objects.get(id = id)
    mensaje = Mensaje.objects.create(
        usuario = usuario,
        mensaje = request.POST['mensaje'],
    )
    return redirect('/wall')

def crearComentario(request, id):
    mensaje = Mensaje.objects.get(id = id)
    usuario_comentador = User.objects.get(id = request.session['usuario']['id'])
    comentario = Comentario.objects.create(
        mensaje = mensaje,
        comentario = request.POST['comentario'],
        usuario = usuario_comentador,
    )
    print(request.POST)
    print(usuario_comentador)
    return redirect('/wall')