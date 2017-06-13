# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0010_auto_20170613_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officelocations',
            old_name='office_location',
            new_name='office_location0',
        ),
    ]
