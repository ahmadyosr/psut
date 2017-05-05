# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_instructor_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='doorsheet',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
