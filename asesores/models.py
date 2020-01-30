# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now
from genero.models import Genero
from municipio.models import Municipio
from comision.models import Comisiones
from perfil_asesor.models import Perfilasesor

class AsesoresDb(models.Model):
    cod_asesor = models.AutoField(primary_key=True, verbose_name='Codigo')
    nombre = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nombres Asesor')
    apellido = models.CharField(max_length=20, blank=True, null=True, verbose_name='Apellidos Asesor')
    direccion = models.CharField(max_length=154, blank=True, null=True, verbose_name='Dirección')
    ciudad = models.ForeignKey(Municipio, db_column='ciudad', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Ciudad', related_name='AsesoresDb.ciudad+')
    direccion2 = models.CharField(max_length=154, blank=True, null=True, verbose_name='Dirección 2')
    ciudad2 = models.ForeignKey(Municipio, db_column='ciudad2', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Ciudad 2', related_name='AsesoresDb.ciudad2+')
    celular = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número de Celular')
    mail = models.CharField(max_length=50, blank=True, null=True, verbose_name='E-Mail')
    t_asesor = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número de Teléfono')
    comision = models.ForeignKey(Comisiones, db_column='comision', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Comision')
    cedula = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número de Cedula')
    c_cedula = models.CharField(max_length=150, blank=True, null=True, verbose_name='Copia de Cedula')
    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Fecha de Registro')
    fecha_s = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Fecha de Actualización')
    perfil = models.ForeignKey(Perfilasesor, db_column='perfil', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Perfil del Asesor')
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True, verbose_name='fecha de Nacimiento')  # Field name made lowercase.
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True, verbose_name='Fecha de Expedición')  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey(Municipio, db_column='ciudadExpedicion', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Ciudad de Expedición')  # Field name made lowercase.
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, db_column='genero')
    cod_ciudad = models.CharField(max_length=15, blank=True, null=True)
    departamento = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asesores_db'
        verbose_name= 'Asesor/Referenciador'
        verbose_name_plural ='Asesores/Referenciadores'
        ordering = ["cod_asesor"]

    def __str__(self):
        #return self.nombre #+ ' ' + self.apellido
        return '%s - %s' % (self.nombre, self.apellido)
        
    def save(self, *args, **kwargs):
        self.cod_ciudad = self.ciudad.codigo_dane
        self.departamento = self.ciudad.departamento
        super(AsesoresDb, self).save(*args, **kwargs)


   