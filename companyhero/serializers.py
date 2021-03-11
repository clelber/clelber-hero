from rest_framework import serializers

from empresas.models import Empresa
from funcionarios.models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = (
            'id',
            'nome',
            'cpf',
            'empresas'
        )


class EmpresaSerializer(serializers.ModelSerializer):
    funcionarios = FuncionarioSerializer(many=True, read_only=True)
    class Meta:
        model = Empresa
        fields = (
            'id',
            'nome',
            'cnpj',
            'ativo',
            'criacao',
            'atualizacao',
            'funcionarios'
        )