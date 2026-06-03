# puerto/views/capitan.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from puerto.models import Capitan
from puerto.serializers import CapitanSerializer
from puerto.permissions import IsStaffOrReadOnly
from puerto.pagination import StandardPagination
from puerto.filters import CapitanFilter


class CapitanViewSet(viewsets.ModelViewSet):
    queryset = Capitan.objects.all()
    serializer_class = CapitanSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CapitanFilter
    search_fields = ['nombres', 'apellidos', 'licencia_navegacion']
    ordering_fields = ['apellidos', 'nombres']
    ordering = ['apellidos', 'nombres']

