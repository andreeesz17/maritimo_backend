# puerto/views/inspeccion.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from puerto.models import Inspeccion
from puerto.serializers import InspeccionSerializer
from puerto.permissions import IsStaffOrReadOnly
from puerto.pagination import StandardPagination
from puerto.filters import InspeccionFilter


class InspeccionViewSet(viewsets.ModelViewSet):
    queryset = Inspeccion.objects.select_related(
        'atraque',
        'atraque__buque',
        'atraque__muelle',
        'atraque__capitan'
    ).all()
    serializer_class = InspeccionSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = InspeccionFilter
    search_fields = ['observaciones', 'atraque__buque__nombre']
    ordering_fields = ['fecha_inspeccion', 'resultado']
    ordering = ['-fecha_inspeccion']

