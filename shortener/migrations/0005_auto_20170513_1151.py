# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-13 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20170513_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yurchikurl',
            name='short_url',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
