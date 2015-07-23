# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0010_auto_20150714_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True, verbose_name='Last Modified')),
                ('title', models.CharField(verbose_name='Tag Title', max_length=255)),
                ('description', models.TextField(verbose_name='Tag Description')),
            ],
            options={
                'abstract': False,
                'get_latest_by': ('last_modified',),
            },
        ),
    ]
