# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_schemas', '0006_auto_20171207_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Er skemaet aktivt?'),
        ),
    ]