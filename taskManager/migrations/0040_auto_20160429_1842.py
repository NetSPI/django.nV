# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0039_auto_20160429_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2016, 5, 6, 18, 42, 26, 963430, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2016, 5, 6, 18, 42, 26, 965504, tzinfo=utc)),
        ),
    ]
