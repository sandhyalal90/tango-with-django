# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150912_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='best',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
