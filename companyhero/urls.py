
from django.contrib import admin
from django.urls import path, include
from funcionarios.urls import router_funcionario
from empresas.urls import router

urlpatterns = [
    path('api/ev1/', include(router.urls)),
    path('api/fv1/', include(router_funcionario.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
