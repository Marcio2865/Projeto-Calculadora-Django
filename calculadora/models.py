from django.db import models
from django.contrib.auth.models import User


class Calculo(models.Model):
    OPERACOES = [
        ('soma', 'Soma (+)'),
        ('subtracao', 'Subtração (-)'),
        ('multiplicacao', 'Multiplicação (*)'),
        ('divisao', 'Divisão (/)'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calculos', null=True, blank=True)
    numero1 = models.FloatField(verbose_name="Primeiro número")
    numero2 = models.FloatField(verbose_name="Segundo número")
    operacao = models.CharField(max_length=20, choices=OPERACOES, verbose_name="Operação")
    resultado = models.FloatField(verbose_name="Resultado", blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data do cálculo")

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Cálculo"
        verbose_name_plural = "Cálculos"

    def __str__(self):
        return f"{self.numero1} {self.get_operacao_display()} {self.numero2} = {self.resultado}"

    def calcular(self):
        numero1 = float(self.numero1)
        numero2 = float(self.numero2)

        if self.operacao == 'soma':
            self.resultado = numero1 + numero2
        elif self.operacao == 'subtracao':
            self.resultado = numero1 - numero2
        elif self.operacao == 'multiplicacao':
            self.resultado = numero1 * numero2
        elif self.operacao == 'divisao':
            if numero2 != 0:
                self.resultado = numero1 / numero2
            else:
                self.resultado = None
        return self.resultado

    def save(self, *args, **kwargs):
        self.calcular()
        super().save(*args, **kwargs)