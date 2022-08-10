from django.contrib import admin
from django.urls import path,include
from banco.views import ConsultaUserViewset, ContaBancariaViewSet, UsuarioViewSet, ConsultaSaldoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='Usuarios')
router.register('contaBancaria', ContaBancariaViewSet, basename='ContaBancaria')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('SaldoBancario/<int:pk>/Saldo/', ConsultaSaldoViewSet.as_view()),
    path('Usuario/<int:pk>/Tipo/', ConsultaUserViewset.as_view())

]