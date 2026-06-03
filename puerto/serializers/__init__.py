# puerto/serializers/__init__.py
from .puerto import PuertoSerializer
from .muelle import MuelleSerializer
from .buque import BuqueSerializer
from .capitan import CapitanSerializer
from .atraque import AtraqueSerializer
from .inspeccion import InspeccionSerializer

__all__ = [
    'PuertoSerializer',
    'MuelleSerializer',
    'BuqueSerializer',
    'CapitanSerializer',
    'AtraqueSerializer',
    'InspeccionSerializer',
]
