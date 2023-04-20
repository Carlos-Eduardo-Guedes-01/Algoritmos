from django.db import models
import sys
sys.path.append("")
class secao(models.Model):
    nome_secao=models.CharField(max_length=50)
    def __str__(self):
        return self.nome_secao
class produtos(models.Model):
    nome_produto=models.CharField(max_length=100)
    secao=models.ForeignKey(secao,on_delete=models.CASCADE)
    empresa=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.nome_produto
    