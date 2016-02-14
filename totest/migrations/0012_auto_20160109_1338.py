# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0011_auto_20160101_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='httpinterfaceinfo',
            name='interface_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
