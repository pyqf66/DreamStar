# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0012_auto_20160109_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='crmmockpaydata',
            name='growthlevel',
            field=models.CharField(default='V1', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crmmockpaydata',
            name='growthvalue',
            field=models.CharField(default=100, max_length=32),
            preserve_default=False,
        ),
    ]
