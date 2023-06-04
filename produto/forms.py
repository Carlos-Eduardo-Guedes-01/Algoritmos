from django import forms
from produto.models import produtos,preco

class ProdutoForm(forms.ModelForm):
    class Meta:
        model=produtos
        fields='__all__'
        widgets={
            'nome_produto':forms.TextInput(attrs={
                'class':'campo','placeholder':'Nome do produto',}),
            'secao':forms.Select(attrs={ 'class': 'campo'}),
            'preco':forms.Select(attrs={'class':'campo','placeholder':'Preço do produto'}),
            'empresa':forms.TextInput(attrs={
                'class':'campo','placeholder':'Empresa Pertencente'}),
            'imagem':forms.FileInput(attrs={ 'class': 'campo'}),
            'empresa':forms.Select(attrs={'class': 'campo'})
        }
class PrecoForm(forms.ModelForm):
    class Meta:
        model=preco
        fields='__all__'
        widgets={
            'valor':forms.NumberInput(attrs={
                'class':'campo','placeholder':'Valor do Preço','style':'margin-top:0;'})
        }