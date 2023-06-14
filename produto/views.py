from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from produto.forms import ProdutoForm,PrecoForm
from .models import *
import sys
sys.path.append("")
from produto.models import *
from empresa.models import *
from .models import preco
import imghdr
def cad_prod(request):
    data={}
    data['title']='Cadastro de Produtos'
    if(request.POST):
        data['form']=ProdutoForm(request.POST, request.FILES)
        form=data['form']
        if(data['form'].is_valid()):
            nome=Empresa.objects.get(id=request.POST.get('empresa'))
            quant=nome.quant_prod
            print(nome.pacote)
            pac=nome.quant_prod
            if(quant<pac):
                quant+=1
                teste=Empresa.objects.filter(nome_empresa=nome).update(quant_prod=quant)
                produto = data['form'].save(commit=False)
                img = request.FILES
                dados_img = imghdr.what(img['imagem'])
                print(dados_img)
                if dados_img == 'png' or dados_img == 'jpeg' or dados_img =='jpg' or dados_img =='webp':
                    
                    data['form'].save()
                    data['msg'] = 'Produto Cadastrado com Sucesso!'
                    data['class'] = 'alert-success'''
                else:
                    data['msg'] = 'Formato de imagem não suportado.'
                    data['class'] = 'alert-danger'''
            elif(quant>=pac):
                data['msg'] = 'Limite do pacote atingido.'
                data['class'] = 'alert-danger'''
        else:
            data['msg'] = 'Formulário inválido.'
            data['class'] = 'alert-danger'''
    else:
        data['form'] = ProdutoForm()
        #data['form']=ProdutoForm()
        data['formpreco']=PrecoForm()
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Produtos'
    return render(request,'../../produto/templates/cadastro_prod.html',data)
def cad_preco(request):
    data={}
    data['title']='Cadastro de Produtos'
    if(request.POST):
        data['formpreco']=PrecoForm(request.POST)
        precos=request.POST.get('valor')
        precos=preco.objects.filter(valor=precos)
        if(len(precos)==0):
            teste=data['formpreco'].save()
            if(teste):
                data['msg'] = 'Preço Cadastrado com Sucesso!'
                data['class'] = 'alert-success'''
            else:
                data['msg'] = 'Formulário inválido.'
                data['class'] = 'alert-danger'''
        elif(len(precos)>0):
            data['msg'] = 'Este preço já existe.'
            data['class'] = 'alert-danger'''

    data['form']=ProdutoForm()
    data['formpreco']=PrecoForm()
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Produtos'
    return render(request,'../../produto/templates/cadastro_prod.html',data)
def busca_prod(request):
    data={}
    data['title'] = 'Cadastro de empresas'
    data['link_form'] = '123'
    data['title'] = 'Pesquisa'
    #Este dado é o que fica na barra verde
    data['titulo'] = 'Cadastro Empresa'
    busca=request.POST.get('search')
    data['produtos']=produtos.objects.filter(nome_produto__contains=busca).filter(status=1)
    return render(request,'../../produto/templates/lista_produtos.html',data)
def secoes(request,v):
    data={}
    data['produtos']=produtos.objects.filter(secao__nome_secao=v).filter(status=1)
    data['title'] = v
    data['link_form'] = '123'
    #Este dado é o que fica na barra verde
    data['titulo'] = 'Cadastro Empresa'
    return render(request, '../../produto/templates/lista_produtos.html',data)
def listagem(request):
    data={}
    data['adm']='ok'
    data['t1']='s'
    data['produtos']=produtos.objects.filter(status=1).order_by('nome_produto')
    return render(request, '../../produto/templates/lista_adm.html',data)
def upd_status(request,id):
    data={}
    data['produtos']=produtos.objects.filter(status=1).order_by('nome_produto')
    return render(request,'../../produto/templates/lista_adm.html',data)
def template_altera(request,id):
    data={}
    query=produtos.objects.get(id=id)
    data['form']=ProdutoForm(instance=query)
    data['formpreco']=PrecoForm()
    if(request.POST):
        form=ProdutoForm(request.POST)
        if(form.is_valid()):
            sv=form.save()
            if(sv):
                data['msg'] = 'Produto Alterado com sucesso!'
                data['class'] = 'alert-success'''
            else:
                data['msg'] = 'Produto Não Alterado.'
                data['class'] = 'alert-danger'''
        
    data['id']=id
    return render(request,'../../produto/templates/edita_prod.html',data)