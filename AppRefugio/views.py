from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppRefugio.models import Libro, Disco, Pelicula
from AppRefugio.forms import LibroFormulario, DiscoFormulario, PeliculaFormulario, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

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

#FORMULARIOS PARA LEER
def leer_libros(request):
    libros = Libro.objects.all()
    contexto = {"libros": libros}

    return render(request, "AppRefugio/leerLibros.html", contexto)


#FORMULARIO PARA ELIMINAR
def eliminar_libros(request, libro_titulo):
    libros = Libro.objects.get(titulo = libro_titulo)
    libros.delete()

    libros = Libro.objects.all()
    contexto = {"libros": libros}
    return render(request, "AppRefugio/leerLibros.html", contexto)


#FORMULARIOS PARA EDITAR

def editar_libros(request, libro_titulo):
    libro = Libro.objects.get(titulo = libro_titulo)
    if request.method == "POST":
        mi_formulario = LibroFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            libro.titulo = informacion["titulo"]
            libro.autor = informacion["autor"]
            libro.sinopsis = informacion["sinopsis"]

            libro.save()
            return render(request, "AppRefugio/inicio.html")
    else:
        mi_formulario = LibroFormulario(initial={"titulo": libro.titulo, "autor": libro.autor, "sinopsis": libro.sinopsis})
            
    return render(request, "AppRefugio/editarLibros.html", {"mi_formulario": mi_formulario, "libro_titulo": libro_titulo})




class DiscoListView(ListView):
    model = Disco
    context_object_name = "discos"
    template_name = "AppRefugio/discos_lista.html"

class DiscoDetailView(DetailView):
    model = Disco
    template_name = "AppRefugio/discos_detalle.html"

class DiscoCreateView(CreateView):
    model = Disco
    template_name = "AppRefugio/discos_crear.html"
    success_url = reverse_lazy("ListaDiscos")
    fields = ["titulo", "interprete"]

class DiscoUpdateView(UpdateView):
    model = Disco
    template_name = "AppRefugio/discos_editar.html"
    success_url = reverse_lazy("ListaDiscos")
    fields = ["titulo", "interprete"]

class DiscoDeleteView(DeleteView):
    model = Disco
    template_name = "AppRefugio/discos_borrar.html"
    success_url = reverse_lazy("ListaDiscos")

#
class PeliculaListView(ListView):
    model = Pelicula
    context_object_name = "peliculas"
    template_name = "AppRefugio/peliculas_lista.html"

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "AppRefugio/peliculas_detalle.html"

class PeliculaCreateView(CreateView):
    model = Pelicula
    template_name = "AppRefugio/peliculas_crear.html"
    success_url = reverse_lazy("ListaPeliculas")
    fields = ["titulo", "director", "sinopsis"]

class PeliculaUpdateView(UpdateView):
    model = Pelicula
    template_name = "AppRefugio/peliculas_editar.html"
    success_url = reverse_lazy("ListaPeliculas")
    fields = ["titulo", "director", "sinopsis"]

class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = "AppRefugio/peliculas_borrar.html"
    success_url = reverse_lazy("ListaPeliculas")


# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data.get("username")
#             contrasenia = form.cleaned_data.get("password")
#             user = authenticate(username = usuario, password = contrasenia)

#             login(request, user)
#             return render(request, "AppRefugio/inicio.html", {"mensaje": f'Bienvenido {user.username}'})
#     else:
#         form = AuthenticationForm()
#         return render(request, "AppRefugio/login.html", {"form": form})
    
# def registro(request):
#     if request.method == "POST":
#         form = UserCreationFormCustom(request.POST)
#         if form.is_valid():
#             username= form.cleaned_data["username"]
#             form.save()
#             return render(request, "AppRefugio/inicio.html", {"mensaje": "Usuario creado con éxito."})

#     else:
#         form = UserCreationFormCustom()
#         return render(request, "AppRefugio/registro.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"AppRefugio/inicio.html")
        else:
            return render(request, "AppRefugio/login.html", {"error": "Nombre de usuario o contraseña incorrectos."})
    return render(request, "AppRefugio/login.html")

@login_required
def user_logout(request):
    logout(request)
    return render(request, "AppRefugio/inicio.html")

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppRefugio/login.html")
    else:
        form = UserCreationForm()
    return render(request, "AppRefugio/register.html", {"form": form})

def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if mi_formulario.is_valid():
            if mi_formulario.cleaned_data.get("imagen"):
                usuario.avatar.imagen = mi_formulario.cleaned_data.get("imagen")
                usuario.avatar.save()
            mi_formulario.save()
            return render(request, "AppRefugio/inicio.html")
    else:       
        mi_formulario = UserEditForm(initial={"imagen": usuario.avatar.imagen}, instance= request.user)
    return render(request, "AppRefugio/editarPerfil.html", {"mi_formulario": mi_formulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppRefugio/cambiar_contrasenia.html"
    success_url = reverse_lazy("EditarPerfil")