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
    ciudad = models.ForeignKey(Municipio, db_column='ciudad', blank=True, null=True, on_delete=models.PROTECT, related_name='DbAbogados.ciudad+')
    ciudadnombre = models.CharField(db_column='ciudadNombre', max_length=27, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(max_length=18, blank=True, null=True)
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.ForeignKey(Municipio, db_column='ciudad2', blank=True, null=True, on_delete=models.PROTECT, related_name='DbAbogados.ciudad2+')
    perfil = models.ForeignKey(Perfil, db_column='perfil', blank=True, null=True, on_delete=models.PROTECT)
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
    contacto = models.ForeignKey(OrigenContacto, db_column='contacto', blank=True, null=True, on_delete=models.PROTECT)
    fecha_actualizacion = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Fecha de Actualización') # => se cambio el tipo de dato DateTimeField
    actualizacion = models.ForeignKey(AsesoresDb, db_column='actualizacion', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Nombre del asesor')
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey(Municipio, db_column='ciudadExpedicion', blank=True, null=True, on_delete=models.PROTECT)  # Field name made lowercase.
    genero = models.ForeignKey(Genero, db_column='genero', on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Fecha de Creación') # => se agrego nuevo campo    

    class Meta:
        managed = True
        db_table = 'db_abogados'
        verbose_name = 'Abogado'
        verbose_name_plural = 'Informe de DB_ABOGADOS' 
        ordering = ["codigo"]

    def __str__(self):
        #return self.nombres +" "+ self.apellidos
        return '%s - %s' % (self.nombres, self.apellidos)
    
    def save(self, *args, **kwargs):
        self.ciudadnombre = self.ciudad.municipio
        self.departamento = self.ciudad.departamento
        super(DbAbogados, self).save(*args, **kwargs)

