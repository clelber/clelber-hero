from rest_framework.routers import SimpleRouter
from .views import EmpresaViewSet

router = SimpleRouter()
router.register('empresas', EmpresaViewSet)
