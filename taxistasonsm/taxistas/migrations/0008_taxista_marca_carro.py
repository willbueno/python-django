# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-27 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxistas', '0007_auto_20161127_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxista',
            name='marca_carro',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]