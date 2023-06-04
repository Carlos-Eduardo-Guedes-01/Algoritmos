from .views import *
from django.urls import path
app_name='pacotes'
from django.contrib import admin
urlpatterns = [
    path('lista-pacotes/',lista_pacotes,name='lista-pacotes'),
]