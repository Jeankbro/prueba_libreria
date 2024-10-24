from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    fecha_pub = models.DateField()
    desc = models.TextField()
    cantidad_copias = models.IntegerField()
    imagen = models.ImageField(upload_to='images/')
    estado = models.CharField(max_length=20)