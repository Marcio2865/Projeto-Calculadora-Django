from django.shortcuts import render, redirect, get_object_or_404
from .models import Calculo


def index(request):
    return render(request, 'calculadora/index.html')


def sobre(request):
    return render(request, 'calculadora/sobre.html')


def contato(request):
    return render(request, 'calculadora/contato.html')


# ---------- CRUD do Histórico ----------

# READ (lista) + CREATE
def historico(request):
    if request.method == 'POST':
        numero1 = request.POST.get('numero1')
        numero2 = request.POST.get('numero2')
        operacao = request.POST.get('operacao')

        Calculo.objects.create(
            numero1=numero1,
            numero2=numero2,
            operacao=operacao
        )
        return redirect('calculadora:historico')

    calculos = Calculo.objects.all()
    return render(request, 'calculadora/historico.html', {'calculos': calculos})


# UPDATE
def editar_calculo(request, pk):
    calculo = get_object_or_404(Calculo, pk=pk)

    if request.method == 'POST':
        calculo.numero1 = request.POST.get('numero1')
        calculo.numero2 = request.POST.get('numero2')
        calculo.operacao = request.POST.get('operacao')
        calculo.save()
        return redirect('calculadora:historico')

    return render(request, 'calculadora/editar_calculo.html', {'calculo': calculo})


# DELETE
def excluir_calculo(request, pk):
    calculo = get_object_or_404(Calculo, pk=pk)

    if request.method == 'POST':
        calculo.delete()
        return redirect('calculadora:historico')

    return render(request, 'calculadora/excluir_calculo.html', {'calculo': calculo})