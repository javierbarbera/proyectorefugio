from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "AppRefugio/inicio.html")

def libros(request):
    return render(request, "AppRefugio/libros.html")

def discos(request):
    return render(request, "AppRefugio/discos.html")

def peliculas(request):
    return render(request, "AppRefugio/peliculas.html")

def lib(request):
    return render(request, "AppRefugio/peliculas.html")