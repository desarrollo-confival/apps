from django.contrib import admin
from .models import Comisiones

# Register your models here.

class ComisionesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comisiones, ComisionesAdmin)

