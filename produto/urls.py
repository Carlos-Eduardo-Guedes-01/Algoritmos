from .views import *
from django.contrib import admin
from django.urls import path
app_name='produto'
urlpatterns = [
    path('cadastro-produto/',cad_prod,name='cad_prod'),
    ]