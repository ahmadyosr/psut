# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0009_auto_20170613_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeLocations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='officehours1',
            name='office_hours',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='officehours2',
            name='office_hours2',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_location',
            field=models.ForeignKey(blank=True, to='instructors.OfficeLocations', null=True),
        ),
    ]
