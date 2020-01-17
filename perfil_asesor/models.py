# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Perfilasesor(models.Model):
    codigo = models.AutoField(primary_key=True,verbose_name='Codigo')
    perfil = models.CharField(max_length=50, verbose_name='Perfil Asesor')

    class Meta:
        managed = False
        db_table = 'perfilasesor'
        verbose_name= 'Perfil del Asesores'
        verbose_name_plural='Perfiles de Asesores'

    def __str__(self):
        return self.perfil