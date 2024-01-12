from django.shortcuts import render, redirect
from datetime import datetime, timedelta
import math

from historial.models import Registro
from plazas.models import Plaza
from core.models import Parametro

def index(request):
    registros = Registro.objects.values('hora_ingreso','hora_salida')
    num_vehiculos = registros.count()
    
    plazas = Plaza.objects.values('nombre','estado')
    value = 'valor_hora'
    valor_hora = Parametro.objects.filter(nombre='valor_hora').values('valor')
   
    espacios_libres = 0
    ingresos = 0
    
    #Obtenemos las plazas disponibles
    for plaza in plazas:
        if plaza['estado'] == True:
            espacios_libres += 1
    
    #Obtenemos las horas de cada vehiculo, el parametro de valor por hora para calcular los ingresos totales
    for registro in registros:
        res = registro['hora_salida'] - registro['hora_ingreso']
        horas = math.ceil(res / timedelta(hours=1))
        
        for valor in valor_hora:
            ingresos += horas * int(valor['valor'])     
        
    
    return render(request, 'core/index.html', {
        'registros': registros,
        'espacios': espacios_libres,
        'ingresos': ingresos,
        'num_vehiculos': num_vehiculos,
    })