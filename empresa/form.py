from dataclasses import field
from django import forms
from empresa.models import Empresa

class DadosForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nome_empresa','tipo','cidade','rua','bairro')
        labels={
            'nome_empresa':'',
            'tipo':'',
            'cidade':'',
            'rua': '',
            'bairro': ''
        }
        widgets = {
            'nome_empresa': forms.TextInput(attrs={ 'class': 'campo offset-md-2', 
                                            'placeholder':'Nome da Empresa'}),
            'tipo': forms.Select(attrs={ 'class': 'campo offset-md-2'}),
            'cidade': forms.Select(attrs={ 'class': 'campo offset-md-2'}),
            'rua': forms.TextInput(attrs={ 'class': 'campo offset-md-2', 
                                            'placeholder':'Ex:Rua Adolfo John Terry'}),
            'bairro': forms.TextInput(attrs={ 'class': 'campo offset-md-2', 
                                            'placeholder':'Ex:Centro'}),
            
            
        }