# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20160923_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintanancerequest',
            name='expirationdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 14, 51, 9, 326474)),
        ),
    ]
