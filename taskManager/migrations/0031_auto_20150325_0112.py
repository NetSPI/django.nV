# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0030_auto_20150325_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 1, 12, 9, 915651, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 1, 12, 9, 916963, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
    ]
