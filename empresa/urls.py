from django.contrib import admin
from django.urls import path
from .views import *
app_name='empresa'
urlpatterns = [
    path('cadastro-empresa',template_cad,name='empresa_cad'),
    path('enterprise-list/',lista_empresa,name='lista-empresas'),
    path('editar-empresa/<int:id>/',alterar_dados,name='altera-dados'),
    path('editar-empresa/',alterando,name='alterando'),
    path('apagar-empresa/',upd_status,name='desabilita-dado'),
    path('empresas-desact/',empresa_desact,name='desactvated'),
    ]