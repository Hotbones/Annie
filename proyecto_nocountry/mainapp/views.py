from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html', {})


def searcher(request):
    return render(request, 'mainapp/searcher.html', {})

def perfil_niñera(request):
    return render(request, 'mainapp/perfilniñera.html', {})

def perfil_cliente(request):
    return render(request, 'mainapp/perfilcliente.html', {})