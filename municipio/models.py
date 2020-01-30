# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Municipio(models.Model):
    codigo = models.AutoField(primary_key=True, verbose_name='Codigo')
    codigo_dane = models.CharField(max_length=15, verbose_name='Codigo DANE')
    departamento = models.CharField(max_length=18, verbose_name='Departamento')
    municipio = models.CharField(max_length=27, verbose_name='Ciudad')

    class Meta:
        managed = False
        db_table = 'municipio'
        verbose_name_plural = 'Municipios'
        verbose_name='Municipio'

    def __str__(self):
        #return self.municipio + ' - ' + self.departamento
        #return self.municipio
        return '%s - %s' % (self.municipio, self.departamento)

