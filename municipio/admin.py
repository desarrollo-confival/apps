from django.contrib import admin
from .models import Municipio

# Register your models here.

class MunicipioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Municipio, MunicipioAdmin)