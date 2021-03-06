# Generated by Django 3.1.4 on 2021-02-11 05:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210208_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizacionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jne_idplangobierno', models.IntegerField()),
                ('tipo_eleccion', models.IntegerField()),
                ('ruta_archivo', models.CharField(max_length=250)),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('organizacion_politica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planes', to='api.organizacionpolitica')),
            ],
            options={
                'verbose_name': 'Organizacion Plan',
                'verbose_name_plural': 'Organizacion Plan',
                'db_table': 'organizacion_plan',
            },
        ),
        migrations.CreateModel(
            name='OrganizacionPlanCriterio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jne_idplangobierno', models.IntegerField()),
                ('plan_criterio_id', models.IntegerField()),
                ('puntaje', models.FloatField(null=True)),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Organizacion Plan criterio',
                'verbose_name_plural': 'Organizacion Plan criterio',
                'db_table': 'organizacion_plan_criterio',
            },
        ),
        migrations.CreateModel(
            name='PlanCriterio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('abreviatura', models.CharField(max_length=30)),
                ('peso', models.IntegerField(null=True)),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Plan criterio',
                'verbose_name_plural': 'Plan criterio',
                'db_table': 'plan_criterio',
            },
        ),
        migrations.CreateModel(
            name='OrganizacionPlanDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jne_idplangobierno', models.IntegerField()),
                ('jne_idplangobdimension', models.IntegerField()),
                ('problema', models.CharField(max_length=300)),
                ('objetivo', models.CharField(max_length=300)),
                ('meta', models.CharField(max_length=300)),
                ('indicador', models.CharField(max_length=300)),
                ('dimension_id', models.IntegerField()),
                ('valor', models.IntegerField(null=True)),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_detalles', to='api.organizacionplan')),
                ('plan_criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_detalles', to='api.plancriterio')),
            ],
            options={
                'verbose_name': 'Organizacion Plan detalle',
                'verbose_name_plural': 'Organizacion Plan detalle',
                'db_table': 'organizacion_plan_detalle',
            },
        ),
    ]
