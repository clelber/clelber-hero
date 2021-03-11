from django.db import models


class Base(models.Model):
    criacao = models.DateField(auto_now_add=True)
    atualizacao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Empresa(Base):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)

    class Meta:
        verbose_name = 'Empresa'

    def __str__(self):
        return self.nome
