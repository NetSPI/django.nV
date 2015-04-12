# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0020_auto_20150316_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.date(2015, 3, 27), verbose_name='date due'),
            preserve_default=True,
        ),
    ]
