from django.db import models
from empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    empresas = models.ManyToManyField(Empresa, related_name='funcionarios')
    cpf = models.CharField(max_length=11)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome
