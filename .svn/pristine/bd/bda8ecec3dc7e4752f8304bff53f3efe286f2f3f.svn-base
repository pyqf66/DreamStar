# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0009_crmmockinfo_crmcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='crmMockPayData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('card_no', models.CharField(max_length=255)),
                ('paylog', models.CharField(max_length=2048)),
                ('crmCode', models.CharField(max_length=32)),
            ],
        ),
        migrations.RenameField(
            model_name='crmmockinfo',
            old_name='crmUrI',
            new_name='crmUri',
        ),
    ]
