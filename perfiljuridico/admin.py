from django.contrib import admin
from .models import Perfiljuridico

# Register your models here.
class PerfiljuridicoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Perfiljuridico,PerfiljuridicoAdmin)