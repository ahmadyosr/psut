# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='school',
            field=models.ForeignKey(blank=True, to='instructors.School', null=True),
        ),
    ]
