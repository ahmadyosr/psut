# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0011_auto_20171102_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
