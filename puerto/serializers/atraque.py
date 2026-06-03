# puerto/serializers/atraque.py
from rest_framework import serializers
from puerto.models import Atraque, Buque, Muelle, Capitan
from puerto.serializers.buque import BuqueSerializer
from puerto.serializers.muelle import MuelleSerializer
from puerto.serializers.capitan import CapitanSerializer


class AtraqueSerializer(serializers.ModelSerializer):
    buque = BuqueSerializer(read_only=True)
    buque_id = serializers.PrimaryKeyRelatedField(
        source='buque',
        write_only=True,
        queryset=Buque.objects.all(),
    )
    muelle = MuelleSerializer(read_only=True)
    muelle_id = serializers.PrimaryKeyRelatedField(
        source='muelle',
        write_only=True,
        queryset=Muelle.objects.none(),
    )
    capitan = CapitanSerializer(read_only=True)
    capitan_id = serializers.PrimaryKeyRelatedField(
        source='capitan',
        write_only=True,
        queryset=Capitan.objects.all(),
    )

    class Meta:
        model = Atraque
        fields = [
            'id', 'buque', 'buque_id', 'muelle', 'muelle_id',
            'capitan', 'capitan_id', 'fecha_ingreso', 'fecha_salida', 'estado'
        ]
        read_only_fields = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['muelle_id'].queryset = Muelle.objects.filter(
            estado='activo',
            puerto__estado='activo'
        )

    def validate(self, attrs):
        # Determine the objects (handle both POST/create and PATCH/update)
        # attrs contains the fields being updated/written. For update, we might need to fallback to self.instance
        muelle = attrs.get('muelle')
        if muelle is None and self.instance:
            muelle = self.instance.muelle

        fecha_ingreso = attrs.get('fecha_ingreso')
        if fecha_ingreso is None and self.instance:
            fecha_ingreso = self.instance.fecha_ingreso

        fecha_salida = attrs.get('fecha_salida')
        if fecha_salida is None and self.instance:
            fecha_salida = self.instance.fecha_salida

        # Validation 1: No permitir atraque en muelle inactivo
        if muelle and muelle.estado != 'activo':
            raise serializers.ValidationError({'muelle_id': 'No se permite atraque en muelle inactivo.'})

        # Validation 2: No permitir atraque en puerto inactivo
        if muelle and muelle.puerto.estado != 'activo':
            raise serializers.ValidationError({'muelle_id': 'No se permite atraque en puerto inactivo.'})

        # Validation 3: Fecha de salida no puede ser menor a fecha de ingreso
        if fecha_ingreso and fecha_salida:
            if fecha_salida < fecha_ingreso:
                raise serializers.ValidationError({'fecha_salida': 'La fecha de salida no puede ser menor a la fecha de ingreso.'})

        return attrs
