# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greedy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='greedy.Genre'),
        ),
    ]
