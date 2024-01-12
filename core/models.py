from django.db import models

# Create your models here.

class Parametro(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
     
    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = 'Parametros'
        
    def __str__(self):
        return self.nombre
