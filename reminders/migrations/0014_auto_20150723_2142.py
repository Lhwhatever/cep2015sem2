# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0013_auto_20150723_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasktag',
            name='color_blue',
        ),
        migrations.RemoveField(
            model_name='tasktag',
            name='color_green',
        ),
        migrations.RemoveField(
            model_name='tasktag',
            name='color_red',
        ),
        migrations.AddField(
            model_name='tasktag',
            name='color_hex',
            field=models.CharField(max_length=7, verbose_name='Tag Color', default='#ffffff', validators=[django.core.validators.RegexValidator(regex='#[0-9A-Fa-f]{6}', message='Not a valid color code.')]),
        ),
    ]
