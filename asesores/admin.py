from django.contrib import admin
from .models import AsesoresDb
from genero.admin import GeneroFilter
from perfil_asesor.admin import PerfilAsesorFilter
from municipio.models import Municipio
from .forms import AsesoresForm

# Register your models here.
# ==> para personalizar el filtro - sujeto a revisión

#===========================================================================================================
#=> PERSONALIZANDO ASESORESDB

class AsesoresDbAdmin(admin.ModelAdmin):
    #form = AsesoresForm
    list_display = ('cod_asesor', 'nombre', 'apellido', 'direccion', 'ciudad', 'celular', 't_asesor', 'mail', 'perfil')
    radio_fields = {
        'genero': admin.HORIZONTAL,
        'perfil': admin.HORIZONTAL,
        'comision': admin.HORIZONTAL,
    }
    readonly_fields = ("fecha", "fecha_s", "cod_ciudad", "departamento") 
    #list_filter = ('cod_asesor', 'nombre', 'perfil')
    list_filter = [PerfilAsesorFilter, GeneroFilter]
    autocomplete_fields = [
        'ciudadexpedicion',
        'ciudad',
        'ciudad2'
    ]
    search_fields = [
        'cod_asesor',
        'nombre',
        'apellido',
        'direccion',
        'ciudad__municipio',
        'direccion2',
        'ciudad2__municipio',
        'celular',
        'mail',
        't_asesor',
        'comision__tipo',
        'cedula',
        'c_cedula',
        'fecha',
        'fecha_s',
        'perfil__perfil',
        'fechanacimiento',
        'fechaexpedicion',
        'ciudadexpedicion__municipio',
        'genero__genero',        
    ]
    
    fieldsets = (
        ('Datos Básicos', {
            'fields': ('nombre', 'apellido', 'cedula', 'fechanacimiento', 'fechaexpedicion', 'ciudadexpedicion', 'genero', 'perfil')
        }),

        ('Contacto', {
            'fields': ('celular', 'mail', 't_asesor')
        }),

        ('Localización', {
            'fields': ('direccion', 'ciudad', 'cod_ciudad', 'departamento', 'direccion2', 'ciudad2')
        }),

        ('Información Adicional', {
            'fields': ('comision', 'c_cedula', 'fecha', 'fecha_s')
        }),
    )
    
    # esto es para el debug de error de libreria autocomplete list filter
    class Media:
        pass    

    def actualizar_campos(AsesoresDbAdmin, request, queryset):
        queryset.update(departamento, cod_ciudad)

admin.site.register(AsesoresDb, AsesoresDbAdmin)

