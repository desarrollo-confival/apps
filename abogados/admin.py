from django.contrib import admin
from .models import DbAbogados
from perfil.admin import PerfilFilter
from municipio.admin import MunicipioFilter
from genero.admin import GeneroFilter 

#===========================================================================================================
#=> PERSONALIZANDO ABOGADOS

class DbAbogadosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombres', 'apellidos', 'cedula', 'genero','tarjeta_p', 'fecha_nacimiento', 'direccion', 'ciudadnombre', 'departamento', 'fijo', 'celular', 'e_mail1')   
    list_filter = [PerfilFilter, MunicipioFilter, GeneroFilter]
    autocomplete_fields = [
        'ciudad',
        'ciudad2',
        'ciudadexpedicion',        
    ]
    search_fields = [
        'codigo',
        'nombres',
        'apellidos',
        'cedula',                
        'tarjeta_p',
        'fecha_nacimiento',
        'direccion',
        'ciudad__municipio',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        'ciudadnombre',
        'departamento',
        'direccion2',
        'ciudad2__municipio',
        'perfil__perfil',
        'empresa',
        'celular2',
        'celular1',
        'celular',
        'fijo2',
        'fijo1',
        'fijo',
        'fax',
        'e_mail1',
        'e_mail2',
        'contacto__contacto',
        'fecha_actualizacion',
        'actualizacion__cod_asesor',
        'observaciones',       
        'fechaexpedicion',
        'ciudadexpedicion__municipio',
        'genero__genero',
        'fecha_creacion',
    ]
    
    fieldsets = (
        ('Datos Básicos', {
            'fields': ('codigo','nombres', 'apellidos', 'cedula', 'fecha_nacimiento', 'fechaexpedicion', 'ciudadexpedicion', 'genero', 'perfil', 'tarjeta_p')
        }),

        ('Contacto', {
            'fields': ('celular', 'celular1', 'celular2', 'fijo', 'fijo1', 'fijo2', 'fax', 'e_mail1', 'e_mail2')
        }),

        ('Localización', {
            'fields': ('direccion', 'ciudad', 'ciudadnombre', 'departamento', 'direccion2', 'ciudad2')
        }),

        ('Información Adicional', {
            'fields': ('empresa', 'actualizacion', 'observaciones', 'contacto','fecha_creacion', 'fecha_actualizacion')
        }),
    )

    readonly_fields = ['codigo', 'fecha_creacion', 'fecha_actualizacion', 'ciudadnombre', 'departamento']
    radio_fields = {'genero': admin.HORIZONTAL, 'contacto': admin.HORIZONTAL, 'perfil': admin.HORIZONTAL}
    
    # esto es para el debug de error de libreria autocomplete list filter
    class Media:
        pass

    def actualizar_campos(DbAbogados, request, queryset):
        queryset.update(ciudadnombre, departamento)

admin.site.register(DbAbogados, DbAbogadosAdmin)