from django.shortcuts import render,redirect
from .models import *
import sys
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout, login as auth_login
sys.path.append("")
from produto.models import *
# Método de login page
def login_view(request):
    data = {}
    data['link_cad']="{% url 'accounts:cadastro_template'%}"
    data['nome']='Login'
    data['titulo']='Login'
    data['title']='Login'
    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario_test=User.objects.filter(email=email)
        if usuario_test:
            usuario=User.objects.get(email=email)
            user = authenticate(request, username=usuario.username, password=senha)
            if user is not None:
                #print(jogador.saldo)
                auth_login(request, user)
                return redirect('accounts:index')
            else:
                data['msg'] = 'Senha inválida!'
                data['class'] = 'alert-danger'
        elif(not usuario_test):
            data['msg'] = 'E-mail inválido!'
            data['class'] = 'alert-danger'
    return render(request,'../../accounts/templates/login.html',data)
@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
@login_required(login_url='accounts:login')
def inicio(request):
    data={}
    data['link_cad']="{% url 'accounts:cadastro_template'%}"
    data['nome']='Cadastrar ADM'
    data['titulo']='Página do ADM'
    data['title']='ADM Principal'
    return render(request,'../../accounts/templates/inicio.html',data)
@login_required(login_url='accounts:login')
def cadastro(request):
    data={}
    data['title']='Cadastro ADM'
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro ADM'
    return render(request,'../../accounts/templates/cadastro.html',data)
@login_required(login_url='accounts:login')
def cadastrando(request):
    titulo='Cadastro Administrador'
    data={}
    try:
        usuario_aux = User.objects.get(username=request.POST['user'])
        usuario_aux2= User.objects.filter(password=request.POST['senha'])

        if usuario_aux or usuario_aux2:
            data['msg'] = 'Usuario ou Senha já existem!'
            data['class'] = 'alert-danger'
    except User.DoesNotExist:
        print('senha: ',request.POST.get('email'))

        if request.POST.get('senha')==request.POST.get('senha_repeat'):
            user = User.objects.create_user(username=request.POST.get('user'),email=request.POST.get('email'), first_name=request.POST.get('nome'), password=request.POST.get('senha'))
            query_user=User.objects.get(id=user.id)
            usu= administrador.objects.create(usuario=query_user)
            user.save()
            data['msg'] = 'Usuário cadastrado com sucesso! Faça Login.'
            data['class'] = 'alert-success'''
        else:
            data['msg'] = 'Senhas incompatíveis.'
            data['class'] = 'alert-danger'''
    data['title']='Cadastro Administrador'
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Administrador'
    return render(request,'../../accounts/templates/cadastro.html',data)

def home(request):
    data={}
    data['nome']='Home'
    data['titulo']='Home'
    data['title']='Home'
    data['prods']=produtos.objects.all()
    return render(request,'../../accounts/templates/home.html',data)


def contato(request):
    data={}
    data['nome']='Contato'
    data['titulo']='Contato'
    data['title']='Contato'
    return render(request,'../../accounts/templates/contato.html',data)

def sobre(request):
    data={}
    data['nome']='Sobre'
    data['titulo']='Sobre'
    data['title']='Sobre'
    return render(request,'../../accounts/templates/sobre.html',data)