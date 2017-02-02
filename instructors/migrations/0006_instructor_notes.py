# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_instructor_office_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='notes',
            field=models.CharField(default='ho', max_length=200),
            preserve_default=False,
        ),
    ]
