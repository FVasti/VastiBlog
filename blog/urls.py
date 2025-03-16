from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("agregar-autor/", views.agregar_autor, name="agregar_autor"),
    path("agregar-articulo/", views.agregar_articulo, name="agregar_articulo"),
    path("agregar-comentario/", views.agregar_comentario, name="agregar_comentario"),
    path("buscar/", views.buscar_articulo, name="buscar"),
]
