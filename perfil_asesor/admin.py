from django.contrib import admin
from .models import Perfilasesor
# Register your models here.

class PerfilasesorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Perfilasesor, PerfilasesorAdmin)