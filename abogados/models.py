# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from genero.models import Genero
from origen_contacto.models import OrigenContacto
from municipio.models import Municipio
from perfil.models import Perfil
from asesores.models import AsesoresDb

class DbAbogados(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=51)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)
    tarjeta_p = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudad', blank=True, null=True)
    ciudadnombre = models.CharField(db_column='ciudadNombre', max_length=27, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(max_length=18, blank=True, null=True)
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudad2', blank=True, null=True)
    perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil', blank=True, null=True)
    empresa = models.CharField(max_length=56, blank=True, null=True)
    celular2 = models.CharField(max_length=15, blank=True, null=True)
    celular1 = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    fijo2 = models.CharField(max_length=15, blank=True, null=True)
    fijo1 = models.CharField(max_length=15, blank=True, null=True)
    fijo = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    e_mail1 = models.CharField(max_length=67, blank=True, null=True)
    e_mail2 = models.CharField(max_length=67, blank=True, null=True)
    contacto = models.ForeignKey('OrigenContacto', models.DO_NOTHING, db_column='contacto', blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    actualizacion = models.ForeignKey('AsesoresDb', models.DO_NOTHING, db_column='actualizacion', blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudadExpedicion', blank=True, null=True)  # Field name made lowercase.
    genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = False
        db_table = 'db_abogados'
