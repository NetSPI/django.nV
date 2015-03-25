# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0026_auto_20150324_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assoc_project',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 3, 31, 23, 46, 51, 229443, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 3, 31, 23, 46, 51, 230765, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
