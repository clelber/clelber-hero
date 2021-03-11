from rest_framework.routers import SimpleRouter
from .views import FuncionarioViewSet

router_funcionario = SimpleRouter()
router_funcionario.register('funcionarios', FuncionarioViewSet)