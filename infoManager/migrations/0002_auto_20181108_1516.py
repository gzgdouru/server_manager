# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-08 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serverinfo',
            old_name='sever_type',
            new_name='server_type',
        ),
    ]