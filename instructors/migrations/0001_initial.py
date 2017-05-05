# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department0',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arabic_name', models.CharField(max_length=200)),
                ('english_name', models.CharField(max_length=200, null=True, blank=True)),
                ('email', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200, null=True, blank=True)),
                ('visits', models.IntegerField(default=0)),
                ('doorsheet', models.FileField(null=True, upload_to=b'')),
                ('department', models.ForeignKey(blank=True, to='instructors.Department0', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_hours', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeHours2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_hours2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_hours_1_start',
            field=models.ForeignKey(blank=True, to='instructors.OfficeHours', null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_hours_2_start',
            field=models.ForeignKey(blank=True, to='instructors.OfficeHours2', null=True),
        ),
        migrations.AddField(
            model_name='department0',
            name='school',
            field=models.ForeignKey(to='instructors.School'),
        ),
    ]
