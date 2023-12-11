from django.contrib import admin
from AppRefugio.models import Libro, Disco, Pelicula, Avatar
from AppRefugio import models

# admin.site.register(models.Libro)
# admin.site.register(models.Disco)
# admin.site.register(models.Pelicula)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "sinopsis")
    list_filter = ("titulo", "autor")
    search_fields = ("titulo", "autor")

@admin.register(Disco)
class DiscoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "interprete")
    list_filter = ("titulo", "interprete")
    search_fields = ("titulo", "interprete")

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "director", "sinopsis")
    list_filter = ("titulo", "director")
    search_fields = ("titulo", "director")

admin.site.register(models.Avatar)