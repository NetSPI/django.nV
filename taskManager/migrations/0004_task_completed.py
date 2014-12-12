# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0003_auto_20141028_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
