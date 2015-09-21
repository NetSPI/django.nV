# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0033_auto_20150325_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='reset_token',
            field=models.CharField(max_length=7, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 18, 29, 23, 667247, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 18, 29, 23, 669103, tzinfo=utc), verbose_name='date due'),
        ),
    ]
