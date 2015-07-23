# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0012_tasktag_color_red'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktag',
            name='color_blue',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0, message='Blue cannot be less than 0'), django.core.validators.MaxValueValidator(255, message='Blue cannot be more than 255')], default=255),
        ),
        migrations.AddField(
            model_name='tasktag',
            name='color_green',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0, message='Green cannot be less than 0'), django.core.validators.MaxValueValidator(255, message='Green cannot be more than 255')], default=255),
        ),
        migrations.AlterField(
            model_name='tasktag',
            name='color_red',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0, message='Red cannot be less than 0'), django.core.validators.MaxValueValidator(255, message='Red cannot be more than 255')], default=255),
        ),
    ]
