# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-10 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yurchikurl',
            name='short_url',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
