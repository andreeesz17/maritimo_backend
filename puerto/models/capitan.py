# puerto/models/capitan.py
from django.db import models


class Capitan(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    licencia_navegacion = models.CharField(max_length=50, unique=True)
    nacionalidad = models.CharField(max_length=100)

    class Meta:
        ordering = ['apellidos', 'nombres']
        verbose_name = 'Capitán'
        verbose_name_plural = 'Capitanes'

    def __str__(self):
        return f'{self.apellidos}, {self.nombres}'
