# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_schemas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemaquestion',
            name='is_response_bool',
            field=models.BooleanField(default=False),
        ),
    ]
