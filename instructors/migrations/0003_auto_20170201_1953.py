# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_auto_20170201_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_hour', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='phone_number',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_hours',
            field=models.ManyToManyField(to='instructors.OfficeHours'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='role',
            field=models.ForeignKey(default=1, to='instructors.Role'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='school',
            field=models.ForeignKey(default=1, to='instructors.School'),
            preserve_default=False,
        ),
    ]
