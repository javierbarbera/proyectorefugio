from django.shortcuts import render
from django.http import HttpResponse
from AppRefugio.models import Libro, Disco, Pelicula
from AppRefugio.forms import LibroFormulario, DiscoFormulario, PeliculaFormulario

# Create your views here.

def inicio(request):
    return render(request, "AppRefugio/inicio.html")

def libros(request):
    if request.method == "POST":
        mi_formulario = LibroFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            libro = Libro(titulo = informacion["titulo"],autor = informacion["autor"], sinopsis = informacion["sinopsis"])
            libro.save()
            return render(request, "AppRefugio/inicio.html")
    else:
        mi_formulario = LibroFormulario()
        return render(request, "AppRefugio/libros.html", {"mi_formulario": mi_formulario})

def discos(request):
    if request.method == "POST":
        mi_formulario = DiscoFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            disco = Disco(titulo = informacion["titulo"],interprete = informacion["interprete"])
            disco.save()
            return render(request, "AppRefugio/inicio.html")
    else:
        mi_formulario = DiscoFormulario()
        return render(request, "AppRefugio/discos.html", {"mi_formulario": mi_formulario})

def peliculas(request):
    if request.method == "POST":
        mi_formulario = PeliculaFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            pelicula = Pelicula(titulo = informacion["titulo"],director = informacion["director"], sinopsis = informacion["sinopsis"])
            pelicula.save()
            return render(request, "AppRefugio/inicio.html")
    else:
        mi_formulario = PeliculaFormulario()
        return render(request, "AppRefugio/peliculas.html", {"mi_formulario": mi_formulario})


# def libros_formulario(request):
#     if request.method == "POST":
#         mi_formulario = LibroFormulario(request.POST)
#         print(mi_formulario)

#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#             libro = Libro(titulo = informacion["titulo"],autor = informacion["autor"], sinopsis = informacion["sinopsis"])
#             libro.save()
#             return render(request, "AppRefugio/inicio.html")
#     else:
#         mi_formulario = LibroFormulario()
#         return render(request, "AppRefugio/libros_formulario.html", {"mi_formulario": mi_formulario})

# def discos_formulario(request):
#     if request.method == "POST":
#         mi_formulario = DiscoFormulario(request.POST)
#         print(mi_formulario)

#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#             disco = Disco(titulo = informacion["titulo"],interprete = informacion["interprete"])
#             disco.save()
#             return render(request, "AppRefugio/inicio.html")
#     else:
#         mi_formulario = DiscoFormulario()
#         return render(request, "AppRefugio/discos_formulario.html", {"mi_formulario": mi_formulario})

# def peliculas_formulario(request):
#     if request.method == "POST":
#         mi_formulario = PeliculaFormulario(request.POST)
#         print(mi_formulario)

#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#             pelicula = Pelicula(titulo = informacion["titulo"],director = informacion["director"], sinopsis = informacion["sinopsis"])
#             pelicula.save()
#             return render(request, "AppRefugio/inicio.html")
#     else:
#         mi_formulario = PeliculaFormulario()
#         return render(request, "AppRefugio/peliculas_formulario.html", {"mi_formulario": mi_formulario})

    
def buscar_libros(request):
    return render(request, "AppRefugio/buscar_libros.html")

def buscar(request):
    titulo = request.GET.get("titulo", "")
    if titulo:
        resultados = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, "AppRefugio/resultadosBusqueda.html", {"titulo": titulo, "resultados": resultados})
    else:
        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

