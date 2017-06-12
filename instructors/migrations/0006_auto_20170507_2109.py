# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_auto_20170505_1640'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OfficeHours',
            new_name='OfficeHours1',
        ),
    ]
