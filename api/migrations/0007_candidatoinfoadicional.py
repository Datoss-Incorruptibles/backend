# Generated by Django 3.1.4 on 2021-04-03 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_candidatoproductividad_candidatoproyectoley_proyectoley'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatoInfoAdicional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jne_idhojavida', models.IntegerField()),
                ('jne_idhvinfoadicional', models.IntegerField()),
                ('info_adicional', models.CharField(max_length=1500)),
                ('fecha_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Candidato info adicional',
                'verbose_name_plural': 'Candidato info adicional',
                'db_table': 'candidato_info_adicional',
            },
        ),
    ]