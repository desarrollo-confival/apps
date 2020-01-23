from django.contrib import admin
from .models import Perfilasesor
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.

class PerfilAsesorFilter(AutocompleteFilter):
    title = 'Perfil Asesor' # display title
    field_name = 'perfil' # name of the foreign key field

class PerfilasesorAdmin(admin.ModelAdmin):
    search_fields = [
        'codigo',
        'perfil',
    ]

admin.site.register(Perfilasesor, PerfilasesorAdmin)