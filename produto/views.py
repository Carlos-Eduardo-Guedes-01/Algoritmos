from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from produto.forms import ProdutoForm,PrecoForm
from .models import *
import sys
sys.path.append("")
from empresa.models import *
from .models import preco
import imghdr
def cad_prod(request):
    data={}
    data['title']='Cadastro de Produtos'
    my_object = Empresa.objects.get(pk=24)
    if(request.POST):
        data['form']=ProdutoForm(request.POST, request.FILES)
        form=data['form']
        if(data['form'].is_valid()):
            nome=Empresa.objects.get(id=request.POST.get('empresa'))
            quant=nome.quant_prod
            quant+=1
            teste=Empresa.objects.filter(nome_empresa=nome).update(quant_prod=quant)
            produto = data['form'].save(commit=False)
            img = request.FILES
            dados_img = imghdr.what(img['imagem'])
            if dados_img == 'png' or dados_img == 'jpeg':
                data['form'].save()
                data['msg'] = 'Produto Cadastrado com Sucesso!'
                data['class'] = 'alert-success'''
            else:
                data['msg'] = 'Formato de imagem não suportado.'
                data['class'] = 'alert-danger'''
        else:
            data['msg'] = 'Formulário inválido.'
            data['class'] = 'alert-danger'''
    else:
        data['form'] = ProdutoForm(instance=my_object, initial={'empresa': my_object.nome_empresa})
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
