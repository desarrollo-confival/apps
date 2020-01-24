from django.contrib import admin
from .models import DbAbogados

#===========================================================================================================
#=> PERSONALIZANDO ABOGADOS

class DbAbogadosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombres', 'apellidos', 'cedula', 'tarjeta_p', 'fecha_nacimiento', 'direccion', 'ciudadnombre', 'departamento', 'fijo', 'celular', 'e_mail1')   
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
        'perfil',
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
        'contacto',
        'fecha_actualizacion',
        'actualizacion',
        'observaciones',       
        'fechaexpedicion',
        'ciudadexpedicion__municipio',
        'genero__genero',
        'fecha_creacion',
    ]
    
    fieldsets = (
        ('Datos Básicos', {
            'fields': ('nombres', 'apellidos', 'cedula', 'fecha_nacimiento', 'fechaexpedicion', 'ciudadexpedicion', 'genero', 'perfil', 'tarjeta_p', 'empresa')
        }),

        ('Contacto', {
            'fields': ('celular', 'celular1', 'celular2', 'fijo', 'fijo1', 'fijo2', 'fax', 'e_mail1', 'e_mail2', 'contacto')
        }),

        ('Localización', {
            'fields': ('direccion', 'ciudad', 'ciudadnombre', 'departamento', 'direccion2', 'ciudad2')
        }),

        ('Información Adicional', {
            'fields': ('actualizacion', 'observaciones')
        }),
    )

    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    radio_fields = {'genero': admin.HORIZONTAL, 'contacto': admin.HORIZONTAL, 'perfil': admin.HORIZONTAL}
    

admin.site.register(DbAbogados, DbAbogadosAdmin)