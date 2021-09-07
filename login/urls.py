from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index),
    path('registrar/', views.registrar),
    path('login/', views.login),
    path('success/', views.success),
    path('logout/', views.logout),
    path('editar/', views.editar),
    # pasar a la dir editar el argumento de id <int:id>
]
