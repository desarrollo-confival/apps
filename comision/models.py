# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comisiones(models.Model):
    codigo = models.AutoField(primary_key=True, verbose_name='Codigo')
    tipo = models.CharField(max_length=15, blank=True, null=True, verbose_name='Tipo de Comision')
    descripcion = models.CharField(max_length=20, blank=True, null=True, verbose_name='Descripción')
    valor = models.FloatField(blank=True, null=True, verbose_name='Valor Comsión')

    class Meta:
        managed = False
        db_table = 'comisiones'
        verbose_name='Comision del Asesor'
        verbose_name_plural='Comisiones de los Asesores'

    def __str__(self):
        return self.tipo

