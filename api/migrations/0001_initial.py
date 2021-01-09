# Generated by Django 3.1.4 on 2021-01-09 01:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=150)),
                ('estado', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('alerta', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'indicador',
            },
        ),
        migrations.CreateModel(
            name='IndicadorCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('alerta', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('order', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.indicador')),
            ],
            options={
                'db_table': 'indicador_categoria',
            },
        ),
        migrations.CreateModel(
            name='OrganizacionPolitica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('fundacion_fecha', models.DateField(null=True)),
                ('estado', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('ruta_archivo', models.CharField(max_length=500)),
                ('jne_idorganizacionpolitica', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('url', models.CharField(max_length=150)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'organizacion_politica',
            },
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.IntegerField()),
                ('jne_idproceso', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'proceso',
            },
        ),
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('ubigeo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=150)),
                ('distrito_electoral', models.CharField(max_length=150)),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'ubigeo',
            },
        ),
        migrations.CreateModel(
            name='IndicadorCategoriaOrganizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('porcentaje', models.FloatField()),
                ('alerta', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.indicador')),
                ('indicador_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.indicadorcategoria')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicadorescategoriaorg', to='api.organizacionpolitica')),
            ],
            options={
                'db_table': 'indicador_categoria_organizacion',
            },
        ),
    ]
