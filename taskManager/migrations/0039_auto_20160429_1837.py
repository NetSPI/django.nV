# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0038_auto_20150921_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 6, 18, 37, 55, 937322, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 6, 18, 37, 55, 939853, tzinfo=utc), verbose_name='date due'),
        ),
    ]
