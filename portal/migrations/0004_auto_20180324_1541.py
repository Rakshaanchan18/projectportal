# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-24 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20180324_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.Project'),
        ),
    ]
