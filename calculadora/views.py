from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Calculo


def index(request):
    return render(request, 'calculadora/index.html')


def sobre(request):
    return render(request, 'calculadora/sobre.html')


def contato(request):
    return render(request, 'calculadora/contato.html')


# ---------- CRUD do Histórico ----------

@login_required
def historico(request):
    if request.method == 'POST':
        numero1 = request.POST.get('numero1')
        numero2 = request.POST.get('numero2')
        operacao = request.POST.get('operacao')

        Calculo.objects.create(
            numero1=numero1,
            numero2=numero2,
            operacao=operacao,
            usuario=request.user
        )
        return redirect('calculadora:historico')

    calculos = Calculo.objects.filter(usuario=request.user)

    operacao_filtro = request.GET.get('operacao')
    if operacao_filtro:
        calculos = calculos.filter(operacao=operacao_filtro)

    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    if data_inicio:
        calculos = calculos.filter(data_criacao__date__gte=data_inicio)
    if data_fim:
        calculos = calculos.filter(data_criacao__date__lte=data_fim)

    contexto = {
        'calculos': calculos,
        'operacao_filtro': operacao_filtro,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }
    return render(request, 'calculadora/historico.html', contexto)


@login_required
def editar_calculo(request, pk):
    calculo = get_object_or_404(Calculo, pk=pk)

    if request.method == 'POST':
        calculo.numero1 = request.POST.get('numero1')
        calculo.numero2 = request.POST.get('numero2')
        calculo.operacao = request.POST.get('operacao')
        calculo.save()
        return redirect('calculadora:historico')

    return render(request, 'calculadora/editar_calculo.html', {'calculo': calculo})


@login_required
def excluir_calculo(request, pk):
    calculo = get_object_or_404(Calculo, pk=pk)

    if request.method == 'POST':
        calculo.delete()
        return redirect('calculadora:historico')

    return render(request, 'calculadora/excluir_calculo.html', {'calculo': calculo})


@user_passes_test(lambda u: u.is_staff)
def listagem_completa(request):
    calculos = Calculo.objects.all()
    return render(request, 'calculadora/listagem_completa.html', {'calculos': calculos})