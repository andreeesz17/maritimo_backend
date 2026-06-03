# puerto/serializers/muelle.py
from rest_framework import serializers
from puerto.models import Muelle, Puerto
from puerto.serializers.puerto import PuertoSerializer


class MuelleSerializer(serializers.ModelSerializer):
    puerto = PuertoSerializer(read_only=True)
    puerto_id = serializers.PrimaryKeyRelatedField(
        source='puerto',
        write_only=True,
        queryset=Puerto.objects.none(),
    )

    class Meta:
        model = Muelle
        fields = ['id', 'puerto', 'puerto_id', 'codigo', 'capacidad_atraque', 'estado']
        read_only_fields = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['puerto_id'].queryset = Puerto.objects.filter(estado='activo')

    def validate_capacidad_atraque(self, value):
        if value < 0:
            raise serializers.ValidationError('La capacidad de muelle no puede ser negativa.')
        return value

    def validate(self, attrs):
        # Even if not filtered in queryset (e.g. for updates or validation logic), check that the puerto is active
        puerto = attrs.get('puerto')
        if puerto and puerto.estado != 'activo':
            raise serializers.ValidationError({'puerto_id': 'No se puede asociar un muelle a un puerto inactivo.'})
        return attrs
