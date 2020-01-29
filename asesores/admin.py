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
    readonly_fields = ("fecha", "fecha_s") 
    #list_filter = ('cod_asesor', 'nombre', 'perfil')
    list_filter = [PerfilAsesorFilter, GeneroFilter]
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

    # def save_model(self, request, obj, form, changue):
    #     # if not obj.ciudad.codigo:
    #     #     obj.ciudad = request.Municipio.municipio
    #     # ojb.cod_ciudad = request.Municipio.codigo
    #     # ojb.departamento = request.Municipio.departamento
    #     # obj.save()

    # def save_model(self, request, obj, form, changue):
    #     """ Autofill in ciudad when blank on save models. """
    #     obj.cod_ciudad = request.user
    #     #obj.departamento = request.user
    #     obj.save()
    # EndDef

    # def save_formset(self, request, form, formset, change):
    #     """ Autofill in ciudad when blank on save formsets. """
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         instance.cod_ciudad = request.cod_ciudad
    #         instance.save()
    #     formset.save_m2m()
    # EndDef
# EndClass


    # esto es para el debug de error de libreria autocomplete list filter
    class Media:
        pass    

    def make_deparatamento(AsesoresDbAdmin, request, queryset):
        queryset.update(departamento, cod_ciudad)

admin.site.register(AsesoresDb, AsesoresDbAdmin)

