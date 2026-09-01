from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Perfil


class CustomLoginView(LoginView):
    pass


class CustomLogoutView(LogoutView):
    next_page = 'calculadora:index'


@login_required
def editar_perfil(request):
    perfil, criado = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        if 'avatar' in request.FILES:
            perfil.avatar = request.FILES['avatar']
            perfil.save()
        return redirect('contas:editar_perfil')

    return render(request, 'contas/editar_perfil.html', {'perfil': perfil})