from dataclasses import field
from django import forms
from empresa.models import Empresa

class DadosForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        labels={
            'nome_empresa':'',
            'tipo':'',
            'cidade':'',
            'rua': '',
            'bairro': ''
        }
        widgets = {
            'nome_empresa': forms.TextInput(attrs={ 'class': 'campo', 
                                            'placeholder':'Nome da Empresa'}),
            'tipo': forms.Select(attrs={ 'class': 'campo'}),
            'cidade': forms.Select(attrs={ 'class': 'campo'}),
            'rua': forms.TextInput(attrs={ 'class': 'campo', 
                                            'placeholder':'Ex:Rua Adolfo John Terry'}),
            'bairro': forms.TextInput(attrs={ 'class': 'campo', 
                                            'placeholder':'Centro'}),
            
        }