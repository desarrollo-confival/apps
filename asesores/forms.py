from django import forms
from municipio.models import Municipio
from .models import AsesoresDb

class AsesoresForm(forms.ModelForm):
    class Meta:
        model = AsesoresDb 
    
    def clean_ciudad(self):
        if not self.cleaned_data['ciudad']:
            return Municipio()
        return self.cleaned_data['ciudad']

    def clean_cod_ciudad(self):
        if not self.cleaned_data['cod_ciudad']:
            return Municipio()
        return self.cleaned_data['cod_ciudad']
    
    def clean_departamento(self):
        if not self.cleaned_data['departamento']:
            return Municipio()
        return self.cleaned_data['departamento']