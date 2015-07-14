# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0009_auto_20150713_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(verbose_name='Completed', default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(verbose_name='Target Date of Completion'),
        ),
    ]
