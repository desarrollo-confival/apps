from django.contrib import admin
from .models import AsesoresDb
# from .models import AsesoresDb, Genero, Municipio, Perfilasesor, Comisiones
# Register your models here.

#admin.site.register(AsesoresDb)
#===========================================================================================================
#=> PERSONALIZANDO ASESORESDB

class AsesoresDbAdmin(admin.ModelAdmin):
    list_display = ('cod_asesor', 'nombre', 'apellido', 'direccion', 'ciudad', 'celular', 't_asesor', 'mail', 'perfil')
    radio_fields = {'genero': admin.HORIZONTAL}
    readonly_fields = ("fecha", "fecha_s") 
    #list_filter = ('cod_asesor', 'nombre')
    # search_fields = [
    #     'cod_asesor',
    #     'nombre',
    #     'apellido',
    #     'direccion',
    #     'ciudad__municipio',
    #     'direccion2',
    #     'ciudad2__municipio',
    #     'celular',
    #     'mail',
    #     't_asesor',
    #     'comision__tipo',
    #     'cedula',
    #     'c_cedula',
    #     'fecha',
    #     'fecha_s',
    #     'perfil__perfil',
    #     'fechanacimiento',
    #     'fechaexpedicion',
    #     'ciudadexpedicion__municipio',
    #     'genero__genero',        
    # ]
    
    # fieldsets = (
    #     ('Datos Básicos', {
    #         'fields': ('nombre', 'apellido', 'cedula', 'fechanacimiento', 'fechaexpedicion', 'ciudadexpedicion', 'genero', 'perfil')
    #     }),

    #     ('Contacto', {
    #         'fields': ('celular', 'mail', 't_asesor')
    #     }),

    #     ('Localización', {
    #         'fields': ('direccion', 'ciudad', 'direccion2', 'cod_ciudad', 'departamento')
    #     }),

    #     ('Información Adicional', {
    #         'fields': ('comision', 'c_cedula', 'fecha', 'fecha_s')
    #     }),
    # )
        
admin.site.register(AsesoresDb, AsesoresDbAdmin)