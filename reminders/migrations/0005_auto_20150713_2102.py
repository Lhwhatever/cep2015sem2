# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0004_auto_20150713_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 13, 2, 37, 387953, tzinfo=utc), verbose_name='Date of Completion'),
        ),
    ]
