from django.db import models
import sys
sys.path.append("")
from empresa.models import *
class secao(models.Model):
    nome_secao=models.CharField(max_length=50)
    def __str__(self):
        return self.nome_secao
class preco(models.Model):
    valor=models.FloatField(null=True)
    def __str__(self):
        return str(self.valor)
class produtos(models.Model):
    nome_produto=models.CharField(max_length=100)
    secao=models.ForeignKey(secao,on_delete=models.CASCADE,verbose_name='Seção',default='Informe a Seção')
    imagem=models.ImageField(upload_to='media')
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, default='Informe o estabelecimento')
    
    preco=models.ForeignKey(preco, on_delete=models.CASCADE, null=True,default='Informe a Preço')
    def __str__(self) -> str:
        return self.nome_produto
    