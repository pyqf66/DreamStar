# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0003_httpinterfaceinfo_interfacename'),
    ]

    operations = [
        migrations.AddField(
            model_name='httpinterfaceinfo',
            name='interfaceCode',
            field=models.CharField(default=datetime.datetime(2015, 11, 14, 6, 43, 58, 944000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
