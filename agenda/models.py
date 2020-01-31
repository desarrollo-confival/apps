# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    recurrence = models.CharField(max_length=1, blank=True, null=True)
    period = models.CharField(max_length=1, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    id_api = models.CharField(max_length=255, blank=True, null=True)
    id_event_google = models.CharField(max_length=255, blank=True, null=True)
    recur_info = models.CharField(max_length=255, blank=True, null=True)
    event_color = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    reminder = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    terminado = models.FloatField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda'

    def __str__(self):
        return self.title