from django.urls import path
from . import views

urlpatterns = [
    path('' , views.wall),
    path('crearMensaje/<int:id>', views.crearMensaje),
    path('crearComentario/<int:id>', views.crearComentario),
]