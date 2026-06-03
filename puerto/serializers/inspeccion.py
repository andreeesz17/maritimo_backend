# puerto/serializers/inspeccion.py
from rest_framework import serializers
from puerto.models import Inspeccion, Atraque
from puerto.serializers.atraque import AtraqueSerializer


class InspeccionSerializer(serializers.ModelSerializer):
    atraque = AtraqueSerializer(read_only=True)
    atraque_id = serializers.PrimaryKeyRelatedField(
        source='atraque',
        write_only=True,
        queryset=Atraque.objects.all(),
    )

    class Meta:
        model = Inspeccion
        fields = ['id', 'atraque', 'atraque_id', 'fecha_inspeccion', 'resultado', 'observaciones']
        read_only_fields = ['id']

    def validate_resultado(self, value):
        valid_results = ['Aprobado', 'Rechazado', 'Pendiente']
        if value not in valid_results:
            raise serializers.ValidationError('El resultado de la inspección debe ser Aprobado, Rechazado o Pendiente.')
        return value
