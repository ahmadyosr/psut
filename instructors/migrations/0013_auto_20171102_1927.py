# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0012_auto_20171102_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='doorsheet',
            field=models.FileField(null=True, upload_to='doorsheets/', blank=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
