from django.contrib import admin
from .models import Genero

# Register your models here.

class GeneroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genero,GeneroAdmin)