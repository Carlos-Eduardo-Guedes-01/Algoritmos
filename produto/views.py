from django.shortcuts import render
from produto.forms import ProdutoForm
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
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Produtos'
    return render(request,'../../produto/templates/cadastro_prod.html',data)
def cadastrando(request):
    data={}
    return render(request,'../../produto/templates/cadastro_prod.html')