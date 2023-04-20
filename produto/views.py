from django.shortcuts import render
def cad_prod(request):
    data={}
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Produtos'
    return render(request,'../../produto/templates/cad_prod.html',data)