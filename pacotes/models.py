from django.db import models
class Pacote(models.Model):
    nome=models.CharField(max_length=100)
    custo=models.FloatField()
    quant_prod=models.IntegerField()
    def __str__(self):
        return self.nome