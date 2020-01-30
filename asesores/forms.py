from django import forms
from municipio.models import Municipio
from .models import AsesoresDb

class AsesoresForm(forms.ModelForm):
#==========================================================================================
#==> Esto para configuraciones de autollenado utilizando plantilla
    class Meta:
        model = AsesoresDb
        fields = [
            'ciudad',
            'cod_ciudad',
            'departamento',
        ]
        labels = {
            'ciudad': 'Ciudad',
            'cod_ciudad': 'Codigo Ciudad',
            'departamento': 'Departamento',
        }
        widgets = {
            #'ciudad': forms.Select(attrs={'class':'form-control'}),
            'cod_ciudad': forms.TextInput(attrs={'class':'form-control'}), 
            'departamento': forms.TextInput(attrs={'class':'form-control'}),            
            # 'departamento': forms.CharField(),
        }