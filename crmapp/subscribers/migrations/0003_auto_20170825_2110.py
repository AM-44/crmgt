# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 18:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_auto_20170825_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name_plural': 'subscribers'},
        ),
    ]
