# puerto/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from puerto.views import (
    health_check,
    PuertoViewSet,
    MuelleViewSet,
    BuqueViewSet,
    CapitanViewSet,
    AtraqueViewSet,
    InspeccionViewSet,
)
from puerto.views.auth import RegisterView, LogoutView
from puerto.serializers.auth import CustomTokenView
from puerto.views.user import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('puertos', PuertoViewSet, basename='puerto')
router.register('muelles', MuelleViewSet, basename='muelle')
router.register('buques', BuqueViewSet, basename='buque')
router.register('capitanes', CapitanViewSet, basename='capitan')
router.register('atraques', AtraqueViewSet, basename='atraque')
router.register('inspecciones', InspeccionViewSet, basename='inspeccion')

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', CustomTokenView.as_view(), name='auth_login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('', include(router.urls)),
]

