# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0014_auto_20150723_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktag',
            name='bgc_hex',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Not a valid color code.', regex='#[0-9A-Fa-f]{6}')], max_length=7, default='#000000', verbose_name='Tag Color'),
        ),
    ]
