from django.db import models

# Create your models here.

#Creación del modelo
class Prueba(models.Model):
    #Se comienzan a agregar los atributos de la clase
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Título: {self.titulo}'