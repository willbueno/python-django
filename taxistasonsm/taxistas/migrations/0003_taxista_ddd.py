# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-27 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxistas', '0002_auto_20161119_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxista',
            name='ddd',
            field=models.IntegerField(default=0),
        ),
    ]
