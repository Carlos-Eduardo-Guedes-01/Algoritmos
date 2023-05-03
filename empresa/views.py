from django.shortcuts import render
from .models import *
from .form import DadosForm
def template_cad (request):
    data={}
    if(request.POST):
        data['form']=DadosForm(request.POST)
        if(data['form'].is_valid()):
            data['form'].save()
            data['msg'] = 'Empresa Cadastrado com Sucesso!'
            data['class'] = 'alert-success'''
        else:
            data['msg'] = 'Formato de imagem não suportado.'
            data['class'] = 'alert-danger'''
    else:
        data['form']=DadosForm()
    data['form']=DadosForm()
    data['title']='Cadastro de empresas'
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Empresa'
    return render(request,'../../empresa/templates/cad_em.html',data)
# Create your views here.
def lista_empresa(request):
    data={}
    data['title']='Lista de Empresas'
    data['nome']='Voltar'
    data['titulo']='Lista de Empresa'
    data['empresas']=Empresa.objects.order_by('nome_empresa')
    data['link_form']="{% url 'accounts:index'%}"
    return render(request,'../../empresa/templates/lista_empresa.html',data)
