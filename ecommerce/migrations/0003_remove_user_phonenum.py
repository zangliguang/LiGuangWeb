# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-19 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20160915_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phonenum',
        ),
    ]
