# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0003_auto_20150713_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(verbose_name='Date of Completion', default=datetime.datetime(2015, 7, 13, 13, 2, 4, 639764, tzinfo=utc)),
        ),
    ]
