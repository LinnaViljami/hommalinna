# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-14 10:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank='true', default=datetime.datetime.now)),
            ],
        ),
    ]
