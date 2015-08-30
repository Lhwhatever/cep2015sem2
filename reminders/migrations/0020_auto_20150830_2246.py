# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0019_auto_20150825_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='private',
        ),
        migrations.RemoveField(
            model_name='tasktag',
            name='private',
        ),
    ]
