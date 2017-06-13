# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0008_auto_20170613_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department0',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='officehours1',
            name='office_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='officehours2',
            name='office_hours2',
            field=models.IntegerField(default=0),
        ),
    ]
