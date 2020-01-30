from django.contrib import admin
from .models import Juridicos

# Register your models here.
class JuridicosAdmin(admin.ModelAdmin):
   
    list_display = ('codigo', 'nombre', 'apellido', 'direccion', 'ciudad', 'mail', 'cedula', 'tarjetaprofesional', 'perfil')
    radio_fields = {
        'genero': admin.HORIZONTAL,
        'perfil': admin.HORIZONTAL,        
    }
    readonly_fields = ("fecha", "fecha_s", "codigo")

    autocomplete_fields = [        
        'ciudad',        
    ]
    search_fields = [
        'codigo',
        'nombre',
        'apellido',
        'direccion',
        'mail',
        'fijo',        
        'cedula',
        'fecha',
        'tarjetaprofesional',
        'fecha_s',
        'perfil__perfil',
        'genero__genero',
        'login',        
    ]
    
    fieldsets = (
        ('Datos Básicos', {
            'fields': ('codigo', 'nombre', 'apellido', 'cedula', 'genero', 'tarjetaprofesional', 'perfil')
        }),

        ('Contacto', {
            'fields': ('mail', 'fijo')
        }),

        ('Localización', {
            'fields': ('direccion', 'ciudad')
        }),

        ('Información Adicional', {
            'fields': ('fecha', 'fecha_s','login')
        }),
    )     

admin.site.register(Juridicos, JuridicosAdmin)