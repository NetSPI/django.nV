# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0031_auto_20150325_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='image_url',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 1, 55, 45, 922156, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 1, 55, 45, 923850, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
