# puerto/models/muelle.py
from django.db import models
from .puerto import Puerto


class Muelle(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    puerto = models.ForeignKey(
        Puerto,
        on_delete=models.PROTECT,
        related_name='muelles',
    )
    codigo = models.CharField(max_length=50)
    capacidad_atraque = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Muelle'
        verbose_name_plural = 'Muelles'

    def __str__(self):
        return f'{self.codigo} ({self.puerto.nombre})'
