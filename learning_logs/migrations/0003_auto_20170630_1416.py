# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_auto_20170630_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='get_topic_entries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.Topic'),
        ),
    ]
