from django.contrib import admin
from .models import AsesoresDb
from perfil_asesor.admin import PerfilAsesorFilter
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.
# ==> para personalizar el filtro - sujeto a revisión

#===========================================================================================================
#=> PERSONALIZANDO ASESORESDB

class AsesoresDbAdmin(admin.ModelAdmin):
    list_display = ('cod_asesor', 'nombre', 'apellido', 'direccion', 'ciudad', 'celular', 't_asesor', 'mail', 'perfil')
    radio_fields = {
        'genero': admin.HORIZONTAL,
        'perfil': admin.HORIZONTAL,
        'comision': admin.HORIZONTAL,
    }
    readonly_fields = ("fecha", "fecha_s") 
    #list_filter = ('cod_asesor', 'nombre', 'perfil')
    list_filter = [PerfilAsesorFilter, 'cod_asesor']
    autocomplete_fields = [
        'ciudadexpedicion',
        'ciudad',
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
            'fields': ('direccion', 'ciudad', 'direccion2', 'cod_ciudad', 'departamento')
        }),

        ('Información Adicional', {
            'fields': ('comision', 'c_cedula', 'fecha', 'fecha_s')
        }),
    )

    # esto es para el debug de error de libreria autocomplete list filter
    class Media:
        pass
        
admin.site.register(AsesoresDb, AsesoresDbAdmin)

