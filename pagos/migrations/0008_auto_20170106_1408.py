# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-06 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0007_auto_20161122_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnor',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='donnor',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='donnor',
            name='country',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='donnor',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='donnor',
            name='zip_code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
