from django.urls import path
from AppRefugio import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("libros/", views.libros, name="libros"),
    path("discos/", views.discos, name="discos"),
    path("peliculas/", views.peliculas, name="peliculas"),


]