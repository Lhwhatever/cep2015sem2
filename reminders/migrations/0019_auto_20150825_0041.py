# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0018_auto_20150825_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='private',
            field=models.BooleanField(default=False, verbose_name='Private'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasktag',
            name='private',
            field=models.BooleanField(default=False, verbose_name='Private'),
            preserve_default=False,
        ),
    ]
