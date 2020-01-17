from django.contrib import admin
from .models import ClaseDocumento

# Register your models here.

class ClaseDocumentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClaseDocumento,ClaseDocumentoAdmin)