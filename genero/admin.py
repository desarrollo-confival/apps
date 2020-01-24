from django.contrib import admin
from .models import Genero
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.

class GeneroFilter(AutocompleteFilter):
    title = 'Genero' # display title
    field_name = 'genero' # name of the foreign key field

class GeneroAdmin(admin.ModelAdmin):
    search_fields = [
        'codigo',
        'genero',
        'abreviatura',
    ]

admin.site.register(Genero,GeneroAdmin)