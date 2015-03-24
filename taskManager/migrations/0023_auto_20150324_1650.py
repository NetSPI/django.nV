# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0022_auto_20150322_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 16, 50, 26, 144258, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 16, 50, 26, 145898, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
    ]
