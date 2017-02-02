# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0007_auto_20170202_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='school',
            field=models.ForeignKey(blank=True, to='instructors.School', null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
