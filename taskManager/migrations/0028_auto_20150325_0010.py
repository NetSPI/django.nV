# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0027_auto_20150324_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='note_text',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 0, 10, 47, 126609, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 0, 10, 47, 128757, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
