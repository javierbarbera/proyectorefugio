from django.urls import path
from AppRefugio import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("libros/", views.libros, name="libros"),
    path("discos/", views.discos, name="discos"),
    path("peliculas/", views.peliculas, name="peliculas"),
    path("librosFormulario/", views.libros_formulario, name="libros formulario"),
    path("discosFormulario/", views.discos_formulario, name="discos formulario"),
    path("peliculasFormulario/", views.peliculas_formulario, name="peliculas formulario"),


]