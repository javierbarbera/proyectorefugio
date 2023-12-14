from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Libro(models.Model):
    titulo= models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.DateField(verbose_name='Fecha de entrada', default=datetime.date.today)
    autor= models.CharField(max_length=50)
    sinopsis= models.TextField()        
    imagen = models.ImageField(upload_to="libros_imagenes/", null=True, blank=True)
    autor_entrada = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return f"Libro"
    
    def imagen_url(self):
        if self.imagen:
            return self.imagen.url
        return None
        

class Disco(models.Model):
    titulo= models.CharField(max_length=50)
    interprete= models.CharField(max_length=50)
 
    def __str__(self):
        return f"Título: {self.titulo} - Interprete: {self.interprete}"

class Pelicula(models.Model):
    titulo= models.CharField(max_length=50)
    director= models.CharField(max_length=50)
    sinopsis= models.TextField()
    
    def __str__(self):
        return f"Título: {self.titulo} - Director: {self.director} - Sinopsis: {self.sinopsis}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"