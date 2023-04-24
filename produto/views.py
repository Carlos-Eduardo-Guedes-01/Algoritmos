from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from produto.forms import ProdutoForm,PrecoForm
from .models import *
from .models import preco
import imghdr
def cad_prod(request):
    data={}
    if(request.POST):
        data['form']=ProdutoForm(request.POST, request.FILES)
        if(data['form'].is_valid()):
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
        data['form']=ProdutoForm()
        data['formpreco']=PrecoForm()
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Produtos'
    return render(request,'../../produto/templates/cadastro_prod.html',data)
def cad_preco(request):
    data={}
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
'''def autocomplete(request):
    if 'term' in request.GET:
        prod = preco.objects.filter(nome__contains=request.GET.get('term'))
        nomes=list()
        for produto in prod:
            nomes.append(preco.valor)
        return JsonResponse(nomes, safe=False)
    return HttpResponse(prod)'''