# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('reminders', '0017_auto_20150818_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(to='accounts.UserProfile', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tasktag',
            name='owner',
            field=models.ForeignKey(to='accounts.UserProfile', null=True, blank=True),
        ),
    ]
