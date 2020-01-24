from django.contrib import admin
from .models import Subitemseguimiento

# Register your models here.

class SubitemseguimientoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subitemseguimiento, SubitemseguimientoAdmin)