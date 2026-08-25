from django.shortcuts import render

def index(request):
    return render(request, 'calculadora/index.html')

def sobre(request):
    return render(request, 'calculadora/sobre.html')

def contato(request):
    return render(request, 'calculadora/contato.html')
