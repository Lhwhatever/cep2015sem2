# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_auto_20150713_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'get_latest_by': ('last_modified',), 'ordering': ('date_end',), 'verbose_name': 'task', 'verbose_name_plural': 'tasks'},
        ),
        migrations.AddField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 12, 58, 39, 179717, tzinfo=utc), verbose_name='Date of Completion'),
        ),
        migrations.AddField(
            model_name='task',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 12, 59, 28, 384074, tzinfo=utc), auto_now_add=True, verbose_name='Last Modified'),
            preserve_default=False,
        ),
    ]
