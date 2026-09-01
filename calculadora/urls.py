from django.urls import path
from . import views

app_name = 'calculadora'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('historico/', views.historico, name='historico'),
    path('historico/editar/<int:pk>/', views.editar_calculo, name='editar_calculo'),
    path('historico/excluir/<int:pk>/', views.excluir_calculo, name='excluir_calculo'),
    path('listagem-completa/', views.listagem_completa, name='listagem_completa'),
]