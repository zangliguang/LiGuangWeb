# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-02 09:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProject',
            fields=[
                ('bid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='Default Business Name', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'User List',
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('sex', models.SmallIntegerField(default=0)),
                ('birthday', models.DateField(default=datetime.datetime.now)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User List',
                'verbose_name': 'User',
            },
        ),
    ]
