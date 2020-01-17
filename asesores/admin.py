from django.contrib import admin
from .models import AsesoresDb
# Register your models here.

class AsesoresDbAdmin(admin.ModelAdmin):
    pass

admin.site.register(AsesoresDb, AsesoresDbAdmin)