# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0016_auto_20141227_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='notes',
        ),
        migrations.AddField(
            model_name='notes',
            name='task',
            field=models.ForeignKey(default=1, to='taskManager.Task'),
            preserve_default=True,
        ),
    ]
