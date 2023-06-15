from .views import *
from django.contrib import admin
from django.urls import path
app_name='produto'
urlpatterns = [
    path('cadastro-produto/',cad_prod,name='cad_prod'),
    path('cadastro-preco/',cad_preco,name='cad-preco'),
    path('search-product/',busca_prod,name='busca-produto'),
    path('secoes/<str:v>/',secoes,name='secoes'),
    path('lista-produtos/',listagem,name='lista-produtos'),
    path('edita-prod/<int:id>/',template_altera,name='altera-dados'),
    #path('alterando/<int:id>/',alterando,name='alterando'),
    path('desabilitado/',upd_status,name='desabilita-dado'),
    #path('deactivated/',listagem_desact,name='desactvated')
    #path('busca-autocomplete/', autocomplete,name='autocomplete'),
    ]
