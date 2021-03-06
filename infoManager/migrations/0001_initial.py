# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-08 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='服务器名称')),
                ('host', models.CharField(max_length=128, unique=True, verbose_name='服务器ip')),
                ('port', models.PositiveIntegerField(verbose_name='服务器端口')),
                ('sever_type', models.CharField(max_length=64, verbose_name='服务器类型')),
            ],
            options={
                'db_table': 'tb_server_info',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.TextField(verbose_name='密码')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infoManager.ServerInfo', verbose_name='所属服务器')),
            ],
            options={
                'db_table': 'tb_user_info',
            },
        ),
    ]
