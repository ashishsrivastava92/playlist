# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greedy', '0005_auto_20160427_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='context',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
