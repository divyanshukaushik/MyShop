# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-30 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20191129_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
