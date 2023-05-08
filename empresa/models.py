from django.db import models
class Tipos(models.Model):
   nome_tipo = models.CharField(max_length=50,default='Selecione o Tipo')
   def __str__(self) -> str:
      return self.nome_tipo

class Estado(models.Model):
   nome_estado = models.CharField(max_length=100)
   uf = models.CharField(max_length=3)
   def __str__(self) -> str:
      return self.uf

class Cidade(models.Model):
   nome_cidade = models.CharField(max_length=100)
   uf = models.ForeignKey(Estado, on_delete=models.CASCADE)
   def __str__(self):
      return ''+str(self.nome_cidade)+'-'+str(self.uf)
   

class Empresa(models.Model):
   nome_empresa = models.CharField(max_length=100)
   tipo =  models.ForeignKey(Tipos, on_delete=models.CASCADE,default='Informe o Tipo')
   cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,default='Informe a Cidade')
   rua = models.CharField(max_length=255)
   bairro = models.CharField(max_length=255)
   quant_prod=models.IntegerField(blank=True, default=0)
   def __str__(self) -> str:
      return self.nome_empresa
   
   
