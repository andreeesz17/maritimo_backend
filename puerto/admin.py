# puerto/admin.py
from django.contrib import admin
from puerto.models import Puerto, Muelle, Buque, Capitan, Atraque, Inspeccion


@admin.register(Puerto)
class PuertoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ciudad', 'capacidad_maxima_buques', 'estado']
    list_filter = ['estado', 'ciudad']
    search_fields = ['nombre', 'ciudad']


@admin.register(Muelle)
class MuelleAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'puerto', 'capacidad_atraque', 'estado']
    list_filter = ['estado', 'puerto']
    search_fields = ['codigo', 'puerto__nombre']


@admin.register(Buque)
class BuqueAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'matricula', 'tipo_buque', 'capacidad_carga', 'pais_origen']
    list_filter = ['tipo_buque', 'pais_origen']
    search_fields = ['nombre', 'matricula']


@admin.register(Capitan)
class CapitanAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombres', 'apellidos', 'licencia_navegacion', 'nacionalidad']
    list_filter = ['nacionalidad']
    search_fields = ['nombres', 'apellidos', 'licencia_navegacion']


@admin.register(Atraque)
class AtraqueAdmin(admin.ModelAdmin):
    list_display = ['id', 'buque', 'muelle', 'capitan', 'fecha_ingreso', 'fecha_salida', 'estado']
    list_filter = ['estado', 'muelle', 'buque', 'capitan']
    search_fields = ['buque__nombre', 'muelle__codigo', 'capitan__apellidos']


@admin.register(Inspeccion)
class InspeccionAdmin(admin.ModelAdmin):
    list_display = ['id', 'atraque', 'fecha_inspeccion', 'resultado']
    list_filter = ['resultado']
    search_fields = ['observaciones', 'atraque__buque__nombre']
