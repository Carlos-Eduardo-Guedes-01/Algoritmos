from django import forms
from produto.models import produtos,preco

class ProdutoForm(forms.ModelForm):
    class Meta:
        model=produtos
        fields='__all__'
        widgets={
            'nome_produto':forms.TextInput(attrs={
                'class':'campo','placeholder':'Nome do produto',}),
            'secao':forms.Select(attrs={ 'class': 'campo','style':'width: 95%;margin-top:0;'}),
            'preco':forms.Select(attrs={'class':'campo','placeholder':'Preço do produto','style':'width:300;'}),
            'empresa':forms.TextInput(attrs={
                'class':'campo','placeholder':'Empresa Pertencente','style':'margin-top:0;'}),
            'imagem':forms.FileInput(attrs={ 'class': 'campo','style':'padding-bottom:0.5%;padding-top:0.4%;'}),
        }
class PrecoForm(forms.ModelForm):
    class Meta:
        model=preco
        fields='__all__'
        widgets={
            'valor':forms.NumberInput(attrs={
                'class':'campo','placeholder':'Valor do Preço','style':'margin-top:0;'})
        }