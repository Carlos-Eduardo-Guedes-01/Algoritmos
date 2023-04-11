from django.shortcuts import render
def cadastro(request):
    return render(request,'../../accounts/templates/cadastro.html')