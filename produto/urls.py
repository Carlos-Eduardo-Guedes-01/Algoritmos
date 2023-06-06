from .views import *
from django.contrib import admin
from django.urls import path
app_name='produto'
urlpatterns = [
    path('cadastro-produto/',cad_prod,name='cad_prod'),
    path('cadastro-preco/',cad_preco,name='cad-preco'),
    path('search-product/',busca_prod,name='busca-produto'),
    path('secoes/<str:v>/',secoes,name='secoes')
    #path('busca-autocomplete/', autocomplete,name='autocomplete'),
    ]
