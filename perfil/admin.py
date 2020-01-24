from django.contrib import admin
from .models import Perfil
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.
class PerfilFilter(AutocompleteFilter):
    title = 'Perfil' # display title
    field_name = 'perfil' # name of the foreign key field

class PerfilAdmin(admin.ModelAdmin):
    search_fields = [
        'codigo',
        'perfil',
    ]
admin.site.register(Perfil, PerfilAdmin)