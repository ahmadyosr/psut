# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0006_instructor_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='role',
            field=models.ForeignKey(blank=True, to='instructors.Role', null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
