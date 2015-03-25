# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0025_auto_20150324_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_text',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 23, 42, 49, 96716, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 23, 42, 49, 98078, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
    ]
