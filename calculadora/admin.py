from django.contrib import admin
from .models import Calculo

@admin.register(Calculo)
class CalculoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'numero1', 'operacao', 'numero2', 'resultado', 'data_criacao')
    list_filter = ('operacao', 'data_criacao', 'usuario')
    search_fields = ('usuario__username', 'numero1', 'numero2')
    ordering = ('-data_criacao',)
    list_per_page = 20
    readonly_fields = ('resultado', 'data_criacao')
