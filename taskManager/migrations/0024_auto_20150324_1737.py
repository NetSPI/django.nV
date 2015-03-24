# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0023_auto_20150324_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 17, 37, 37, 425854, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 17, 37, 37, 427415, tzinfo=utc), verbose_name='date due'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.CharField(max_length=3000, default=''),
            preserve_default=True,
        ),
    ]
