# puerto/views/puerto.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from puerto.models import Puerto
from puerto.serializers import PuertoSerializer
from puerto.permissions import IsStaffOrReadOnly
from puerto.pagination import StandardPagination
from puerto.filters import PuertoFilter


class PuertoViewSet(viewsets.ModelViewSet):
    queryset = Puerto.objects.all()
    serializer_class = PuertoSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PuertoFilter
    search_fields = ['nombre', 'ciudad']
    ordering_fields = ['nombre', 'capacidad_maxima_buques']
    ordering = ['nombre']

