from django.shortcuts import render
from StoreApp.models import Departamento, Produto

# Create your views here.
def index(request):
    produtos_em_destaque = Produto.objects.filter(destaque = True)

    context = {
        'produtos' : produtos_em_destaque
    }
    return render(request, 'index.html', context)

def produto_lista(request):
    #Buscar produto no banco
    produtos = Produto.objects.all()

    context = {
        'produtos' : produtos,
        'categoria' : 'Todos Produtos',
    }
    return render(request, 'produtos.html', context)

def produto_lista_por_id(request, id):
    #Buscar produto no banco
    produtos = Produto.objects.filter(departamento_id = id)
    #Buscar departamento no banco
    departamento = Departamento.objects.get(id = id)


    context = {
        'produtos' : produtos,
        'categoria' : departamento.nome,
    }
    return render(request, 'produtos.html', context)


def produto_detalhe(request, id):
    #Buscar produto no banco
    produto = Produto.objects.get(id = id)
    produtos_relacionados =  Produto.objects.filter(departamento_id = produto.departamento.id).exclude(id = id)[:4]

    context = {
        'produto' : produto,
        'produtos_relacionados' : produtos_relacionados
    }

    return render(request, 'produto_detalhes.html', context)

def institucional(request):
    return render(request, 'sobre.html')