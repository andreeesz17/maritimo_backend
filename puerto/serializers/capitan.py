# puerto/serializers/capitan.py
from rest_framework import serializers
from puerto.models import Capitan


class CapitanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitan
        fields = ['id', 'nombres', 'apellidos', 'licencia_navegacion', 'nacionalidad']
        read_only_fields = ['id']
