# puerto/models/atraque.py
from django.db import models
from .buque import Buque
from .muelle import Muelle
from .capitan import Capitan


class Atraque(models.Model):
    ESTADO_CHOICES = [
        ('programado', 'Programado'),
        ('en_curso', 'En Curso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    buque = models.ForeignKey(
        Buque,
        on_delete=models.PROTECT,
        related_name='atraques',
    )
    muelle = models.ForeignKey(
        Muelle,
        on_delete=models.PROTECT,
        related_name='atraques',
    )
    capitan = models.ForeignKey(
        Capitan,
        on_delete=models.PROTECT,
        related_name='atraques',
    )
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='programado')

    class Meta:
        ordering = ['-fecha_ingreso']
        verbose_name = 'Atraque'
        verbose_name_plural = 'Atraques'

    def __str__(self):
        return f'Atraque {self.id} - Buque: {self.buque.nombre} en Muelle: {self.muelle.codigo}'
