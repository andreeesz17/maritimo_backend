# puerto/views/atraque.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from puerto.models import Atraque
from puerto.serializers import AtraqueSerializer
from puerto.permissions import IsStaffOrReadOnly
from puerto.pagination import StandardPagination
from puerto.filters import AtraqueFilter


class AtraqueViewSet(viewsets.ModelViewSet):
    queryset = Atraque.objects.select_related('buque', 'muelle', 'capitan', 'muelle__puerto').all()
    serializer_class = AtraqueSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AtraqueFilter
    search_fields = ['buque__nombre', 'muelle__codigo', 'capitan__apellidos']
    ordering_fields = ['fecha_ingreso', 'fecha_salida', 'estado']
    ordering = ['-fecha_ingreso']

