# Generated by Django 2.2.6 on 2020-01-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juridicos',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=154, null=True)),
                ('mail', models.CharField(blank=True, max_length=50, null=True)),
                ('fijo', models.CharField(blank=True, max_length=15, null=True)),
                ('cedula', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('tarjetaprofesional', models.CharField(blank=True, db_column='tarjetaProfesional', max_length=30, null=True)),
                ('fecha_s', models.DateField(blank=True, null=True)),
                ('login', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'juridicos',
                'managed': False,
            },
        ),
    ]
