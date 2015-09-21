# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0036_auto_20150921_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 25, 51, 222213, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 25, 51, 223982, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='reset_token_expiration',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 20, 25, 51, 220866, tzinfo=utc)),
        ),
    ]
