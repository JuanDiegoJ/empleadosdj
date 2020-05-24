from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Áreas de la empresa'
        # ordering = [Nombre del atributo por el que se quiere ordenar]
        ordering = ['name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.name
