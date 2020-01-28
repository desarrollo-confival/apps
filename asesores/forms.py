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



#==========================================================================================
#==> Esto para configuraciones de rest django

    # class Meta:
    #     model = AsesoresDb
    #     fields = [
    #         'ciudad',
    #         'cod_ciudad',
    #         'departamento',
    #     ]
    #     labels = {
    #         'ciudad': 'Ciudad',
    #         'cod_ciudad': 'Codigo Ciudad',
    #         'departamento': 'Departamento',
    #     }
    #     widgets = {
    #         'ciudad': forms.Select(attrs={'class':'form-control'}),
    #         'cod_ciudad': forms.TextInput(attrs={'class':'form-control'}), 
    #         'departamento': forms.TextInput(attrs={'class':'form-control'}),            
    #         # 'departamento': forms.CharField(),
    #     }