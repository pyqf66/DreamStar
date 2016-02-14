# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('totest', '0005_auto_20151114_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='address_city',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=40)),
                ('provinceCode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='address_province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='address_town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=40)),
                ('cityCode', models.CharField(max_length=6)),
            ],
        ),
    ]
