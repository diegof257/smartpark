from django.db import models

# Create your models here.

class Registro(models.Model):
    placa = models.CharField(max_length=255)
    hora_ingreso = models.DateTimeField()
    hora_salida = models.DateTimeField(blank=True, null=True)
    pago_total = models.IntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ('hora_ingreso',)
        verbose_name_plural = 'Registros'
        
    def __str__(self):
        return self.placa