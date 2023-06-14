from .views import *
from django.urls import path
from django.contrib import admin
app_name='pacotes'
urlpatterns = [
    path('Cadastro-pacotes/',cad_pac,name='cadastro-pac'),
    path('lista-pacotes/',lista_pacotes,name='lista-pacotes'),
    path('editar-pacotes/<int:id>/',template_editar,name='template-edita'),
    path('editar-pacotes/altearando/',alterando,name='alterando'),
]