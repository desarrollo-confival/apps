from django.contrib import admin
from .models import Desicion
# Register your models here.

class DesicionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Desicion, DesicionAdmin)