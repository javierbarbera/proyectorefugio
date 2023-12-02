from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo= models.CharField(max_length=50)
    autor= models.CharField(max_length=50)
    sinopsis= models.TextField()

class Disco(models.Model):
    titulo= models.CharField(max_length=50)
    interprete= models.CharField(max_length=50)
 
class Pelicula(models.Model):
    titulo= models.CharField(max_length=50)
    director= models.CharField(max_length=50)
    sinopsis= models.TextField()