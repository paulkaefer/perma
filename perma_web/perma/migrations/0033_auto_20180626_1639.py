# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0032_capturejob_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallinkuser',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='linkuser',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]