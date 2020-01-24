from django.contrib import admin
from .models import Municipio
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.

class MunicipioFilter(AutocompleteFilter):
    title = 'Municipio' # display title
    field_name = 'ciudad' # name of the foreign key field

class MunicipioAdmin(admin.ModelAdmin):
    search_fields = [
        'codigo',
        'codigo_dane',
        'departamento',
        'municipio',
    ]
    ordering = ['codigo']

admin.site.register(Municipio, MunicipioAdmin)