# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topx', '0006_auto_20160727_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='num_antendidas',
            new_name='num_atendidas',
        ),
    ]
