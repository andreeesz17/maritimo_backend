# puerto/serializers/buque.py
from rest_framework import serializers
from puerto.models import Buque


class BuqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buque
        fields = ['id', 'nombre', 'matricula', 'tipo_buque', 'capacidad_carga', 'pais_origen']
        read_only_fields = ['id']

    def validate_capacidad_carga(self, value):
        if value <= 0:
            raise serializers.ValidationError('La capacidad de carga del buque debe ser mayor a cero.')
        return value
