# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0007_auto_20170507_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department0',
            name='title',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
