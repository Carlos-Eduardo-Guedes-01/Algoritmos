import os
from django.shortcuts import render
from django.templatetags.static import static
import io
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from datetime import date
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle,Image
from core import settings
from produto.forms import ProdutoForm,PrecoForm
from .models import *
from django.shortcuts import get_object_or_404
import sys
sys.path.append("")
from produto.models import *
from empresa.models import *
from accounts.models import *
from .models import preco
from django.contrib.auth.decorators import login_required
import imghdr

@login_required(login_url='accounts:login')
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
@login_required(login_url='accounts:login')
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
    data = {}
    data['title'] = 'Cadastro de empresas'
    data['link_form'] = '123'
    data['title'] = 'Pesquisa'
    data['titulo'] = 'Cadastro Empresa'
    busca = request.POST.get('search')
    
    data['produtos'] = produtos.objects.raw(
        "SELECT produto.id, produto.nome_produto, secao.nome_secao, empresa.nome_empresa, "
        "MAX(preco.valor) AS maior_preco, MIN(preco.valor) AS menor_preco, produto.imagem "
        "FROM produto_produtos AS produto "
        "INNER JOIN produto_secao AS secao ON produto.secao_id = secao.id "
        "INNER JOIN empresa_empresa AS empresa ON produto.empresa_id = empresa.id "
        "INNER JOIN produto_preco AS preco ON produto.preco_id = preco.id "
        "WHERE produto.nome_produto LIKE %s AND produto.status = 1 "
        "GROUP BY produto.nome_produto",
        ['%' + busca + '%']
    )
    return render(request, '../../produto/templates/lista_produtos.html', data)

def secoes(request,v):
    data={}
    secao2=secao.objects.get(nome_secao=v)
    print(secao2.id)
    #data['produtos']=produtos.objects.filter(secao__nome_secao=v).filter(status=1)
    data['produtos'] = produtos.objects.raw(
        "SELECT produto.id, produto.nome_produto, secao.nome_secao, empresa.nome_empresa, "
        "MAX(preco.valor) AS maior_preco, MIN(preco.valor) AS menor_preco, produto.imagem "
        "FROM produto_produtos AS produto "
        "INNER JOIN empresa_empresa AS empresa ON produto.empresa_id = empresa.id "
        "INNER JOIN produto_preco AS preco ON produto.preco_id = preco.id "
        "WHERE produto.secao_id = %s AND produto.status = 1 "
        "GROUP BY produto.nome_produto",
        [secao2.id]
    )
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
@login_required(login_url='accounts:login')
def upd_status(request,id):
    data={}
    data['produtos']=produtos.objects.filter(status=1).order_by('nome_produto')
    return render(request,'../../produto/templates/lista_adm.html',data)
@login_required(login_url='accounts:login')
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
        elif(not form.is_valid()):
            data['msg'] = "O produto não foi alterado \n Formulário inválido ." 
            data['class'] = 'alert-danger'''
    data['id']=id
    return render(request,'../../produto/templates/edita_prod.html',data)
def detalhes(request,titulo,id):
    data = {}
    data['title'] = 'Cadastro de empresas'
    produto = get_object_or_404(produtos, pk=id)
    rel = relatorio(produto=produto, data_busca=date.today())
    rel.save()
    data['link_form'] = '123'
    data['title'] = 'Pesquisa'
    data['titulo'] = 'Cadastro Empresa'
    data['empresas']=produtos.objects.filter(nome_produto=titulo)
    data['produto']=get_object_or_404(produtos,pk=id)
    return render(request,'detalhe_prod.html',data)
def generate_report(request):
     # Cria um file-like buffer para receber os dados do PDF
     
    buffer = io.BytesIO()
    mes=request.POST.get('mes')
    ano=request.POST.get('ano')
    produtos = relatorio.objects.raw(
    "SELECT relatorio.id, relatorio.produto_id, COUNT(relatorio.produto_id) AS total "
    "FROM produto_relatorio AS relatorio, produto_produtos AS produto "
    "WHERE substr(relatorio.data_busca, 6, 2) = %s "
    "AND substr(relatorio.data_busca, 1, 4) = %s "
    "AND relatorio.produto_id = produto.id "
    "GROUP BY relatorio.produto_id",
    [mes, ano]
)

    # Cria o objeto PDF usando o buffer como "arquivo"
    doc = SimpleDocTemplate(buffer, pagesize=letter,topMargin=20)

    # Lista para armazenar os elementos do relatório
    elements = []
    # Obtém o estilo de amostra para os estilos de parágrafo
    styles = getSampleStyleSheet()
    logo_path = os.path.join(settings.BASE_DIR, 'accounts', 'static', 'img', 'logo.png')

    # Verifica se o arquivo da logo existe
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=100, height=100)
        elements.append(logo)
    else:
        pass
    # Adiciona um título ao relatório
    title_text = "Relatório de Produtos RBC"
    title = Paragraph("<b>{}</b>".format(title_text), styles['Title'])
    elements.append(title)

    # Adiciona um parágrafo de introdução

    # Adiciona uma tabela ao relatório
    data = [['Produto', 'Quantidade']]
    
    for produto in produtos:
        produto_data = [produto.produto.nome_produto, produto.total]
        data.append(produto_data)

    column_widths = [300, 100, 100]  # Defina os valores desejados para a largura de cada coluna

    # Cria a tabela e define as larguras das colunas
    table = Table(data, colWidths=column_widths)

    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('FONTSIZE', (0, 0), (-1, 0), 14),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('ALIGN', (-1, 1), (-1, -1), 'CENTER'),
                               ]))
    elements.append(table)

    # Gera o relatório
    doc.build(elements)

    # Coloca o ponteiro do buffer no início
    buffer.seek(0)

    # Cria a resposta HTTP com o conteúdo do arquivo PDF
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

    return response