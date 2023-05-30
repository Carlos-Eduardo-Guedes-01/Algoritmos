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
    data['empresas']=Empresa.objects.filter(status=1).order_by('nome_empresa')
    data['link_form']="{% url 'accounts:index'%}"
    return render(request,'../../empresa/templates/lista_empresa.html',data)
def alterar_dados(request, id):
    data={}
    data['empresa']=Empresa.objects.get(id=id)
    data['tipos']=Tipos.objects.all()
    data['cidades']=Cidade.objects.all()
    data['title']='Editando Empresas'
    print(data['cidades'])
    return render(request,'../../empresa/templates/editar_dados.html',data)
def alterando(request):
    data={}
    nome=request.POST.get('nome_empresa')
    tipo=request.POST.get('tipo')
    cidade=request.POST.get('cidade')
    rua=request.POST.get('rua')
    bairro=request.POST.get('bairro')
    id=request.POST.get('id')
    data['title']='Editando Empresas'
    print(tipo)
    data['empresa']=Empresa.objects.get(id=id)
    emp=Empresa.objects.filter(id=id).update(nome_empresa=nome, tipo=tipo,cidade=cidade,rua=rua,bairro=bairro)
    if(emp):
        data['msg'] = 'Empresa editada com sucesso!'
        data['class'] = 'alert-success'
    else:
        data['class'] = 'alert-danger'
        data['msg']='Falha ao alterar dados!'
    data['tipos']=Tipos.objects.all()
    data['cidades']=Cidade.objects.all()
    data['empresa']=Empresa.objects.get(id=id)
    print(nome,rua,tipo,cidade,bairro)
    return render(request,'../../empresa/templates/editar_dados.html',data)
def upd_status(request):
    data={}
    data={}
    data['title']='Lista de Empresas'
    data['nome']='Voltar'
    data['titulo']='Lista de Empresa'
    data['empresas']=Empresa.objects.filter(status=1).order_by('nome_empresa')
    data['link_form']="{% url 'accounts:index'%}"
    id=request.POST.get('id')
    emp=Empresa.objects.filter(id=id).update(status=0)
    return render(request,'../../empresa/templates/lista_empresa.html',data)