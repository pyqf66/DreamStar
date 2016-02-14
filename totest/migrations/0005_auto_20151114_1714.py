# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0004_httpinterfaceinfo_interfacecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='httpinterfaceinfo',
            name='interfaceId',
            field=models.CharField(default=datetime.datetime(2015, 11, 14, 9, 14, 1, 191000, tzinfo=utc), max_length=30, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='httpinterfaceinfo',
            name='httpInterface',
            field=models.CharField(max_length=300),
        ),
    ]
