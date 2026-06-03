# puerto/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from puerto.views import (
    health_check,
    PuertoViewSet,
    MuelleViewSet,
    BuqueViewSet,
    CapitanViewSet,
    AtraqueViewSet,
    InspeccionViewSet,
)

router = DefaultRouter()
router.register('puertos', PuertoViewSet, basename='puerto')
router.register('muelles', MuelleViewSet, basename='muelle')
router.register('buques', BuqueViewSet, basename='buque')
router.register('capitanes', CapitanViewSet, basename='capitan')
router.register('atraques', AtraqueViewSet, basename='atraque')
router.register('inspecciones', InspeccionViewSet, basename='inspeccion')

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('', include(router.urls)),
]
