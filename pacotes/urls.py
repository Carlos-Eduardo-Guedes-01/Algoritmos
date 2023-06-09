from .views import *
from django.urls import path
app_name='pacotes'
from django.contrib import admin
urlpatterns = [
    path('Cadastro-pacotes/',cad_pac,name='cadastro-pac'),
    path('lista-pacotes/',lista_pacotes,name='lista-pacotes'),
]