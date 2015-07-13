# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0006_auto_20150713_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(verbose_name='Date of Completion', default=datetime.datetime(2015, 7, 13, 13, 3, 21, 486050, tzinfo=utc)),
        ),
    ]
