# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0004_remove_instructor_office_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='office_hours',
            field=models.CharField(default='1', max_length=500),
            preserve_default=False,
        ),
    ]
