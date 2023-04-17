from django.contrib import admin
from django.urls import path
from .views import *
app_name='accounts'
urlpatterns = [
    path('',cadastro,name='cadastro_template'),
    path('cadastrando/',cadastrando,name='cadastrando'),
]