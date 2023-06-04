from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def lista_pacotes(request):
    data={}
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Lista de Pacotes'
    data['title']='Lista de Pacotes'
    return render(request, '../../pacotes/templates/lista_pacotes.html',data)