from django.db import models
class Pacote(models.Model):
    nome=models.CharField(max_length=100, verbose_name='Nome do Pacote')
    custo=models.CharField(verbose_name='Custo do Pacote',max_length=10)
    quant_prod=models.IntegerField(verbose_name='Quantidade de Produtos')
    quant_carousel=models.IntegerField(verbose_name='Quantidade de itens de Carousel',default=0)
    descricao=models.TextField(verbose_name='Descrição do Pacote')
    img=models.ImageField(verbose_name='Animação do Pacote(.gif)',upload_to= 'pacotes/media',default='media/sem_foto.png')
    def __str__(self):
        return self.nome