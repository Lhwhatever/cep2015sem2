# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0016_task_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktag',
            name='abbrev',
            field=models.CharField(max_length=16, verbose_name='Abbreviation', default='ayy'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tasktag',
            name='bgc_hex',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Not a valid color code.', regex='#[0-9A-Fa-f]{6}')], max_length=7, verbose_name='Color (Background)', default='#000000'),
        ),
        migrations.AlterField(
            model_name='tasktag',
            name='color_hex',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Not a valid color code.', regex='#[0-9A-Fa-f]{6}')], max_length=7, verbose_name='Color (Foreground)', default='#ffffff'),
        ),
    ]
