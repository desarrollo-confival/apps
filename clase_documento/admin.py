from django.contrib import admin
from .models import ClaseDocumento

# Register your models here.

class ClaseDocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'tipo_documento',
        'documento',
    )

admin.site.register(ClaseDocumento,ClaseDocumentoAdmin)