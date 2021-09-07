from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages
from datetime import datetime, time, timedelta
from django.utils import timezone

def wall(request):
    if 'usuario' not in request.session:
        return redirect('/')
    else:
        mensajes = Mensaje.objects.all().order_by('-created_at')
        cantMensajes = len(mensajes)
        comentarios = Comentario.objects.all()
        cantComentarios =len(comentarios)
        usuarios = User.objects.all()
        contexto = {
            'mensajes'          : mensajes,
            'comentarios'       : comentarios, 
            'usuarios'          : usuarios,
            'cantMensajes'      : cantMensajes,
            'cantComentarios'   : cantComentarios,
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
    return redirect('/wall')

def minutos(fecha):
    today = timezone.now()
    resultado = (today.year - fecha.year)*365*24*60 + (today.month - fecha.month)*30*24*60 + (today.day - fecha.day)*24*60 + (today.hour-fecha.hour)*60 + (today.minute-fecha.minute)
    return resultado

def delete(request , id):
    usuario = User.objects.get(id = request.session['usuario']['id'])
    mensaje = Mensaje.objects.get(id = id)

    calcular_tiempo = minutos(mensaje.created_at)
    if calcular_tiempo > 30:
        messages.warning(request, "Han pasado mas de 30 min, no puedes borrar el mensaje")
        return redirect('/wall')
    else: 
        messages.success(request ,'Borrado con exito')
        mensaje.delete()
        return redirect("/wall")

