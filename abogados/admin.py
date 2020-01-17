from django.contrib import admin
from .models import DbAbogados

# Register your models here.

class DbAbogadosAdmin(admin.ModelAdmin):
    pass

admin.site.register(DbAbogados, DbAbogadosAdmin)