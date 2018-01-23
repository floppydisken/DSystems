# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_schemas', '0024_auto_20180118_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemahistorylog',
            name='new_schema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='obsolete', to='dynamic_schemas.Schema'),
        ),
        migrations.AlterField(
            model_name='schemahistorylog',
            name='obsolete_schema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='new', to='dynamic_schemas.Schema'),
        ),
    ]