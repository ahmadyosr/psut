# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0009_auto_20171102_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='office_hours_1',
            field=models.TimeField(default=datetime.datetime(2017, 11, 2, 19, 18, 32, 930307, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
