# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0024_auto_20150324_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 3, 31, 23, 40, 33, 763694, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 3, 31, 23, 40, 33, 765148, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
