# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171126_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='setting_id',
            new_name='setting',
        ),
    ]
