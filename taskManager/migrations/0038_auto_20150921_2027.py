# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0037_auto_20150921_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 27, 22, 64757, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 20, 27, 22, 66753, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='reset_token_expiration',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
