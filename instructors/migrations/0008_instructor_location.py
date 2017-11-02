# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0007_auto_20170507_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
