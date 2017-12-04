# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchemaQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_schemas.Schema')),
            ],
        ),
        migrations.CreateModel(
            name='SchemaResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qa_set', jsonfield.fields.JSONField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_schemas.SchemaQuestion')),
            ],
        ),
    ]
