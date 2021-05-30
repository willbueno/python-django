# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-19 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combustivel', models.FloatField()),
                ('valor_combustivel', models.FloatField()),
                ('numero_integrantes', models.IntegerField()),
            ],
        ),
    ]
