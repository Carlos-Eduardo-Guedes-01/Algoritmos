from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .forms import PacoteForm
# Create your views here.
def cad_pac(request):
    data={}
    data['title']='Cadastro de Produtos'
    if(request.POST):
        data['form']=PacoteForm(request.POST)
        form=data['form']
        if(data['form'].is_valid()):
            produto = data['form'].save()
            if(produto):
                data['class']='alert-success'
                data['msg']='Pacote Cadastrado com Sucesso!'
        else:
            data['msg'] = 'Formulário inválido.'
            data['class'] = 'alert-danger'''
    else:
        data['form'] = PacoteForm()
        #data['form']=PacoteForm()
    data['titulo']='Cadastro Pacotes'
    return render(request,'../../pacotes/templates/cad_pacotes.html',data)
def lista_pacotes(request):
    data={}
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Lista de Pacotes'
    data['title']='Lista de Pacotes'
    return render(request, '../../pacotes/templates/lista_pacotes.html',data)