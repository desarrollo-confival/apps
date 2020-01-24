from django import forms
from municipio.models import Municipio
from .models import AsesoresDb

class AsesoresForm(forms.ModelForm):
    class Meta:
        model = AsesoresDb 
        fields = "__all__" 
    
    def clean_ciudad(self):
        if not self.cleaned_data['ciudad']:
            return Municipio('ciudad')
        return self.cleaned_data['ciudad']

    def clean_cod_ciudad(self):
        if not self.cleaned_data['cod_ciudad']:
            return Municipio('cod_ciudad')
        return self.cleaned_data['cod_ciudad']
    
    def clean_departamento(self):
        if not self.cleaned_data['departamento']:
            return Municipio('departamento')
        return self.cleaned_data['departamento']