# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topx', '0011_auto_20160727_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='url_youtube',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
