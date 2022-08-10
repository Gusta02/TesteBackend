from django.contrib import admin
from django.urls import path,include
from banco.views import UsuarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='Usuarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]