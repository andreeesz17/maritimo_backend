# puerto/serializers/puerto.py
from rest_framework import serializers
from puerto.models import Puerto


class PuertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puerto
        fields = ['id', 'nombre', 'ciudad', 'capacidad_maxima_buques', 'estado']
        read_only_fields = ['id']

    def validate_capacidad_maxima_buques(self, value):
        if value < 0:
            raise serializers.ValidationError('La capacidad máxima de buques no puede ser negativa.')
        return value
