from django.urls import reverse
from django.shortcuts import render
from .models import *
from .form import DadosForm
def template_cad(request):
    data = {}
    if request.method == 'POST':
        form = DadosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['msg'] = 'Empresa cadastrada com sucesso!'
            data['class'] = 'alert-success'
        else:
            data['msg'] = 'Formato de imagem não suportado.'
            data['class'] = 'alert-danger'
    else:
        form = DadosForm()
    data['form'] = form
    data['title'] = 'Cadastro de empresas'
    data['link_form'] = reverse('accounts:index')
    data['nome'] = 'Voltar'
    data['titulo'] = 'Cadastro Empresa'
    return render(request, '../../empresa/templates/cad_em.html', data)

# Create your views here.
def lista_empresa(request):
    data={}
    data['title']='Lista de Empresas'
    data['nome']='Voltar'
    data['titulo']='Lista de Empresa'
    data['empresas']=Empresa.objects.order_by('nome_empresa')
    data['link_form']="{% url 'accounts:index'%}"
    return render(request,'../../empresa/templates/lista_empresa.html',data)
