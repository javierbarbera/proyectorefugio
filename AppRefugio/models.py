from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo= models.CharField(max_length=50)
    autor= models.CharField(max_length=50)
    sinopsis= models.TextField()

    def __str__(self):
        return f"Título: {self.titulo} - Autor: {self.autor} - Sinopsis: {self.sinopsis}"
        

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