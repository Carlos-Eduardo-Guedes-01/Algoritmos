from django.contrib import admin
from django.urls import path
from .views import *
app_name='accounts'
urlpatterns = [
    #path('',login_page,name='login_page'),
    path('bla/',inicio,name='index'),
    path('cadastra-adm/',cadastro,name='cadastro_template'),
    path('',home,name='home'),
    path('contato/',contato,name='contato'),
    path('sobre/',sobre,name='sobre'),
    path('cadastrando/',cadastrando,name='cadastrando'),
    path('login/',login,name='login'),
]