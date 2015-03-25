# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0032_auto_20150325_0155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_img',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 1, 59, 31, 58419, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 4, 1, 1, 59, 31, 59855, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
