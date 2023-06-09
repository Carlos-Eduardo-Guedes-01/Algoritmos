from django.db import models
class Pacote(models.Model):
    nome=models.CharField(max_length=100, verbose_name='Nome do Pacote')
    custo=models.FloatField(verbose_name='Custo do Pacote')
    quant_prod=models.IntegerField(verbose_name='Quantidade de Produtos')
    descricao=models.TextField(verbose_name='Descrição do Pacote')
    def __str__(self):
        return self.nome