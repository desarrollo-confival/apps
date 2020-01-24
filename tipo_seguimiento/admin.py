from django.contrib import admin
from .models import TipoSeguimiento

# Register your models here.

class TipoSeguimientoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoSeguimiento, TipoSeguimientoAdmin)
