from django.shortcuts import render
from .models import *
def cadastro(request):
    return render(request,'../../accounts/templates/cadastro.html')
def cadastrando(request):
    print(request.POST.get('email'))
    print(request.POST.get('senha'))
    print(request.POST.get('nome'))
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
    return render(request,'../../accounts/templates/cadastro.html',data)