# app_servicios/models.py

from django.db import models

class Servicio(models.Model):
    # Django crea automáticamente el campo 'id' (id_server) como clave primaria
    nombre_ser = models.CharField(max_length=100, verbose_name="Nombre")
    desc = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio")
    duracion = models.CharField(max_length=50, verbose_name="Duración")
    tipo_de_serv = models.CharField(max_length=100, verbose_name="Tipo de Servicio")

    def __str__(self):
        return self.nombre_ser + f" (${self.precio})"