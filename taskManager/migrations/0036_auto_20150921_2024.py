# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0035_auto_20150921_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 9, 28, 20, 24, 31, 994559, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='date due', default=datetime.datetime(2015, 9, 28, 20, 24, 31, 996298, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='reset_token_expiration',
            field=models.DateTimeField(),
        ),
    ]
