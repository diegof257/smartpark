from django.db import models

# Create your models here.

class TipoPlazas(models.Model):
    descripcion = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('descripcion',)
        verbose_name_plural = 'TipoPlazas'
        
    def __str__(self):
        return self.descripcion

class Plaza(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_plaza = models.ForeignKey(TipoPlazas, related_name='plazas', on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = 'Plazas'
        
    def __str__(self):
        return self.nombre,self.estado
    
    
