# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0010_instructor_office_hours_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='office_hours_1_start',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='office_hours_2_start',
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_hours_2',
            field=models.TimeField(default=datetime.datetime(2017, 11, 2, 19, 24, 43, 308566, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
