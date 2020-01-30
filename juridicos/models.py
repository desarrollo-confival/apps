# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from municipio.models import Municipio
from genero.models import Genero
from perfiljuridico.models import Perfiljuridico


class Juridicos(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey(Municipio, on_delete=models.PROTECT, db_column='ciudad', blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    fijo = models.CharField(max_length=15, blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    tarjetaprofesional = models.CharField(db_column='tarjetaProfesional', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fecha_s = models.DateField(blank=True, null=True)
    perfil = models.ForeignKey(Perfiljuridico, on_delete=models.PROTECT, db_column='perfil', blank=True, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, db_column='genero', blank=True, null=True)
    login = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'juridicos'
        verbose_name= 'Jurídico'
        verbose_name_plural ='Jurídicos'
        ordering = ["codigo"]
    
    def __str__(self):
        return '%s - %s' %(self.nombre, self.apellido)