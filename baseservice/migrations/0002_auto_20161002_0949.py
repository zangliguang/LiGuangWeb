# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-02 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseservice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='common_business_type',
            name='business_tname',
        ),
        migrations.RemoveField(
            model_name='common_business_type',
            name='business_tname2',
        ),
    ]
