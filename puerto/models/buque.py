# puerto/models/buque.py
from django.db import models


class Buque(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True)
    tipo_buque = models.CharField(max_length=50)
    capacidad_carga = models.DecimalField(max_digits=12, decimal_places=2)
    pais_origen = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Buque'
        verbose_name_plural = 'Buques'

    def __str__(self):
        return f'{self.nombre} ({self.matricula})'
