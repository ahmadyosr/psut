# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0013_auto_20171102_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='school',
            new_name='building',
        ),
    ]
