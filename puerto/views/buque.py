# puerto/views/buque.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from puerto.models import Buque
from puerto.serializers import BuqueSerializer
from puerto.permissions import IsStaffOrReadOnly
from puerto.pagination import StandardPagination
from puerto.filters import BuqueFilter


class BuqueViewSet(viewsets.ModelViewSet):
    queryset = Buque.objects.all()
    serializer_class = BuqueSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BuqueFilter
    search_fields = ['nombre', 'matricula']
    ordering_fields = ['nombre', 'capacidad_carga']
    ordering = ['nombre']

