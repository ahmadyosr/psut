# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_auto_20170201_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='office_hours',
        ),
    ]
