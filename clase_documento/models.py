# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from  tipo_documento.models import TipoDocumento


class ClaseDocumento(models.Model):
    codigo = models.AutoField(primary_key=True, verbose_name='Codigo')
    tipo_documento = models.ForeignKey(TipoDocumento, db_column='tipo_documento', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Tipo de Documento')
    documento = models.CharField(max_length=150, blank=True, null=True, verbose_name='Documento')

    class Meta:
        managed = False
        db_table = 'clase_documento'
        verbose_name='Clase de Documento'
        verbose_name_plural='Clases de Documentos'

    def __str__(self):
        return self.documento
