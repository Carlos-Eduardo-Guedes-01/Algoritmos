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
            'imagem':forms.FileInput(attrs={ 'class': 'campo'}),
            'empresa':forms.Select(attrs={'class': 'campo'}),
            'status':forms.TextInput(attrs={'value':'1', 'readonly':'readonly', 'style':'display:none;'}),
            'carousel':forms.RadioSelect(attrs={},choices=[('1','Sim'),('0','Não')])
        }
class PrecoForm(forms.ModelForm):
    class Meta:
        model=preco
        fields='__all__'
        widgets={
            'valor':forms.NumberInput(attrs={
                'class':'campo','placeholder':'Valor do Preço','style':'margin-top:0;'})
        }