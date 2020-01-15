from django.contrib import admin
from .models import OrigenContacto

# Register your models here.

class OrigenContactoAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrigenContacto, OrigenContactoAdmin)