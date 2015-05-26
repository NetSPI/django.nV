# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0020_auto_20150316_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=(timezone.now() + datetime.timedelta(days=7)), verbose_name='date due'),
            preserve_default=True,
        ),
    ]
