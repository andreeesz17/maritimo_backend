# puerto/filters.py
import django_filters
from puerto.models import Puerto, Muelle, Buque, Capitan, Atraque, Inspeccion


class PuertoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    ciudad = django_filters.CharFilter(lookup_expr='icontains')
    capacidad_min = django_filters.NumberFilter(field_name='capacidad_maxima_buques', lookup_expr='gte')
    capacidad_max = django_filters.NumberFilter(field_name='capacidad_maxima_buques', lookup_expr='lte')

    class Meta:
        model = Puerto
        fields = ['estado']


class MuelleFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    capacidad_min = django_filters.NumberFilter(field_name='capacidad_atraque', lookup_expr='gte')
    capacidad_max = django_filters.NumberFilter(field_name='capacidad_atraque', lookup_expr='lte')
    puerto_nombre = django_filters.CharFilter(field_name='puerto__nombre', lookup_expr='icontains')

    class Meta:
        model = Muelle
        fields = ['estado', 'puerto']


class BuqueFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    matricula = django_filters.CharFilter(lookup_expr='icontains')
    tipo_buque = django_filters.CharFilter(lookup_expr='icontains')
    pais_origen = django_filters.CharFilter(lookup_expr='icontains')
    capacidad_carga_min = django_filters.NumberFilter(field_name='capacidad_carga', lookup_expr='gte')
    capacidad_carga_max = django_filters.NumberFilter(field_name='capacidad_carga', lookup_expr='lte')

    class Meta:
        model = Buque
        fields = []


class CapitanFilter(django_filters.FilterSet):
    nombres = django_filters.CharFilter(lookup_expr='icontains')
    apellidos = django_filters.CharFilter(lookup_expr='icontains')
    licencia_navegacion = django_filters.CharFilter(lookup_expr='icontains')
    nacionalidad = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Capitan
        fields = []


class AtraqueFilter(django_filters.FilterSet):
    fecha_ingreso_gte = django_filters.DateTimeFilter(field_name='fecha_ingreso', lookup_expr='gte')
    fecha_ingreso_lte = django_filters.DateTimeFilter(field_name='fecha_ingreso', lookup_expr='lte')
    fecha_salida_gte = django_filters.DateTimeFilter(field_name='fecha_salida', lookup_expr='gte')
    fecha_salida_lte = django_filters.DateTimeFilter(field_name='fecha_salida', lookup_expr='lte')

    class Meta:
        model = Atraque
        fields = ['estado', 'muelle', 'buque', 'capitan']


class InspeccionFilter(django_filters.FilterSet):
    fecha_inspeccion_gte = django_filters.DateTimeFilter(field_name='fecha_inspeccion', lookup_expr='gte')
    fecha_inspeccion_lte = django_filters.DateTimeFilter(field_name='fecha_inspeccion', lookup_expr='lte')

    class Meta:
        model = Inspeccion
        fields = ['resultado', 'atraque']
