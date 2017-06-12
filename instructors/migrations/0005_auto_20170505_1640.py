# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0004_auto_20170505_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='school2',
            new_name='school',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='shool',
        ),
    ]
