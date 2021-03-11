from .models import Empresa
from companyhero.serializers import EmpresaSerializer, FuncionarioSerializer

from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    @action(detail=True, methods=['get'])
    def funcionarios(self, request, pk=None):
        empresa = self.get_object()
        serializer = FuncionarioSerializer(empresa.funcionarios.all(), many=True)
        return Response(serializer.data)



