# puerto/models/inspeccion.py
from django.db import models
from .atraque import Atraque


class Inspeccion(models.Model):
    RESULTADO_CHOICES = [
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
        ('Pendiente', 'Pendiente'),
    ]

    atraque = models.ForeignKey(
        Atraque,
        on_delete=models.CASCADE,
        related_name='inspecciones',
    )
    fecha_inspeccion = models.DateTimeField()
    resultado = models.CharField(max_length=20, choices=RESULTADO_CHOICES, default='Pendiente')
    observaciones = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['-fecha_inspeccion']
        verbose_name = 'Inspección'
        verbose_name_plural = 'Inspecciones'

    def __str__(self):
        return f'Inspección {self.id} - Atraque: {self.atraque.id} ({self.resultado})'
