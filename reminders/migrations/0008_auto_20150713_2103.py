# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0007_auto_20150713_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 13, 3, 39, 418744, tzinfo=utc), verbose_name='Date of Completion'),
        ),
    ]
