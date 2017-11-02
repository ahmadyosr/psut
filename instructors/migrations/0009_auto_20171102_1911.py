# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0008_instructor_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='doorsheet',
            field=models.FileField(null=True, upload_to='doorsheets/'),
        ),
    ]
