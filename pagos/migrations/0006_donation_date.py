# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0005_auto_20161014_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
