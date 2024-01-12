from django.contrib import admin

# Register your models here.

from .models import TipoPlazas
from .models import Plaza

admin.site.register(TipoPlazas)
admin.site.register(Plaza)
