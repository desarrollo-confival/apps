from django.contrib import admin
from .models import TipoDocumento

# Register your models here.

class TipoDocumentoAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoDocumento,TipoDocumentoAdmin)