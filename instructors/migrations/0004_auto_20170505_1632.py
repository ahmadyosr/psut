# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_auto_20170505_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='school',
            new_name='school2',
        ),
        migrations.AddField(
            model_name='instructor',
            name='shool',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
