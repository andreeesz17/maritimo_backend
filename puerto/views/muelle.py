# puerto/views/muelle.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from puerto.models import Muelle
from puerto.serializers import MuelleSerializer
from puerto.permissions import IsStaffOrReadOnly
from puerto.pagination import StandardPagination
from puerto.filters import MuelleFilter


class MuelleViewSet(viewsets.ModelViewSet):
    queryset = Muelle.objects.select_related('puerto').all()
    serializer_class = MuelleSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MuelleFilter
    search_fields = ['codigo', 'puerto__nombre']
    ordering_fields = ['codigo', 'capacidad_atraque']
    ordering = ['codigo']

