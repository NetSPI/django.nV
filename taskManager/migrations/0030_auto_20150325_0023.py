# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0029_auto_20150325_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='pub_date',
            new_name='start_date',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 0, 23, 21, 922798, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 0, 23, 21, 924921, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
