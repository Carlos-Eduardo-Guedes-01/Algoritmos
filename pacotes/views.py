from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import PacoteForm
# Create your views here.
@login_required(login_url='accounts:login')
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
'''def lista_pacotes(request):
    data={}
    data['title']='Lista de Pacotes'
    #Gambiarra de verificação presente no arquivo lista_empresa.html
    data['t1']='v'
    data['titulo']='Lista de Pacotes'
    #Busca de empresas com status ativo e ordenado por nome_empresa
    data['pacotes']=Pacote.objects.order_by('nome')
    #Variável de mensagem da janela modal
    data['msn']='desativar'
    #Texto do botão da janela modal
    data['btn']='Desativar'
    return render(request,'../../pacotes/templates/lista_pacotes.html',data)'''
@login_required(login_url='accounts:login')
def lista_pacotes(request):
    data={}
    data['title']='Lista de Pacotes'
    #Gambiarra de verificação presente no arquivo lista_empresa.html
    data['t1']='v'
    data['titulo']='Lista de Pacotes'
    #Busca de empresas com status ativo e ordenado por nome_empresa
    data['pacotes']=Pacote.objects.order_by('nome')
    #Variável de mensagem da janela modal
    data['msn']='desativar'
    #Texto do botão da janela modal
    data['btn']='Desativar'
    return render(request,'../../pacotes/templates/lista_pacotes.html',data)
@login_required(login_url='accounts:login')
def template_editar(request,id):
    data={}
    #Buscando dados atuais da empresa
    data['pacote']=Pacote.objects.get(id=id)
    data['title']='Editando Pacotes '
    return render(request,'../../pacotes/templates/editar_pacotes.html',data)
@login_required(login_url='accounts:login')
def alterando(request):
    data={}
    # Recebendo dados do formulário
    nome=request.POST.get('nome')
    custo=request.POST.get('custo')
    quant=request.POST.get('quant')
    desc=request.POST.get('desc')
    img=request.POST.get('img')
    id=request.POST.get('id')
    data['title']='Editando Pacotes'
    # Buscando os dados da empresa para filtragem
    data['pacote']=Pacote.objects.get(id=id)
    # Efetivando alterações
    emp=Pacote.objects.filter(id=id).update(nome=nome, custo=custo,quant_prod=quant,descricao=desc,img=img)
    # Verificando se alteração funcionou ou não
    if(emp):
        data['msg'] = 'Pacote editado com sucesso!'
        data['class'] = 'alert-success'
    else:
        data['class'] = 'alert-danger'
        data['msg']='Falha ao alterar dados!'
    data['pacote']=Pacote.objects.get(id=id)
    return render(request,'../../pacotes/templates/editar_pacotes.html',data)