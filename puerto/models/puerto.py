# puerto/models/puerto.py
from django.db import models


class Puerto(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    capacidad_maxima_buques = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Puerto'
        verbose_name_plural = 'Puertos'

    def __str__(self):
        return self.nombre
