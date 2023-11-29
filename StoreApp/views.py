from django.shortcuts import render
from StoreApp.models import Departamento, Produto

# Create your views here.
def index(request):
    return render(request, 'index.html')

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


def produto_detalhe(request):
    return render(request, 'produto_detalhes.html')