# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0028_auto_20150325_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_text',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 0, 15, 53, 427375, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 0, 15, 53, 429537, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
