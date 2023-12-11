from django.urls import path
from AppRefugio import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("libros/", views.libros, name="libros"),
    path("discos/", views.discos, name="discos"),
    path("peliculas/", views.peliculas, name="peliculas"),
    #path("librosFormulario/", views.libros_formulario, name="libros formulario"),
    #path("discosFormulario/", views.discos_formulario, name="discos formulario"),
    #path("peliculasFormulario/", views.peliculas_formulario, name="peliculas formulario"),
    path("buscarLibros/", views.buscar_libros, name="buscar libros"),
    path("buscar/", views.buscar, name = "buscar"),
    path("leerLibros/", views.leer_libros, name = "leerlibros"),
    path('eliminarLibros/<libro_titulo>/', views.eliminar_libros, name="eliminarlibros"),
    path('editarLibros/<libro_titulo>/', views.editar_libros, name="editarlibros"),

    path('discos/lista', views.DiscoListView.as_view(), name = "ListaDiscos"),
    path('discos/nuevo', views.DiscoCreateView.as_view(), name = "NuevoDiscos"),
    path('discos/<pk>', views.DiscoDetailView.as_view(), name = "DetalleDiscos"),
    path('discos/<pk>/editar', views.DiscoUpdateView.as_view(), name = "EditarDiscos"),
    path('discos/<pk>/borrar', views.DiscoDeleteView.as_view(), name = "BorrarDiscos"),

    path('peliculas/lista', views.PeliculaListView.as_view(), name = "ListaPeliculas"),
    path('peliculas/nuevo', views.PeliculaCreateView.as_view(), name = "NuevoPeliculas"),
    path('peliculas/<pk>', views.PeliculaDetailView.as_view(), name = "DetallePeliculas"),
    path('peliculas/<pk>/editar', views.PeliculaUpdateView.as_view(), name = "EditarPeliculas"),
    path('peliculas/<pk>/borrar', views.PeliculaDeleteView.as_view(), name = "BorrarPeliculas"),

    path('login/', views.user_login, name= "user_login"),
    path('register/', views.user_register, name= "user_register"),
    path('logout/', views.user_logout, name ="user_logout"),
    path('editarPerfil/', views.editar_perfil, name ="EditarPerfil"),
    path('cambiarContrasenia/', views.CambiarContrasenia.as_view(), name ="CambiarContrasenia"),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)