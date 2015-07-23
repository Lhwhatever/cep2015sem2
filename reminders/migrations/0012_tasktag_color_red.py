# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0011_tasktag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktag',
            name='color_red',
            field=models.PositiveSmallIntegerField(default=255, max_length=255),
            preserve_default=False,
        ),
    ]
