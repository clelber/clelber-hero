from .models import Funcionario
from companyhero.serializers import FuncionarioSerializer
from rest_framework import viewsets, generics
from django_filters import rest_framework as filters


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class FuncionariosAPIView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

    def get_queryset(self):
        if self.kwargs.get('empresa_pk'):
            return self.queryset.filter(empresas=self.kwargs.get('empresa_pk'))
        return self.queryset.all()

