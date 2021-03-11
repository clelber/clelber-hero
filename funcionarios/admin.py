from django.contrib import admin

from .models import Funcionario


@admin.register(Funcionario)
class Funcionarios(admin.ModelAdmin):
    list_display = ('nome', 'cpf')

