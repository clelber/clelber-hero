from django.contrib import admin

from .models import Empresa


@admin.register(Empresa)
class Empresas(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')
