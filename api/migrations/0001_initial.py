# Generated by Django 3.1.4 on 2021-01-03 06:20

import datetime
from django.db import migrations, models


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
        )

    ]
