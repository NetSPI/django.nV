# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0015_auto_20141224_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='notes',
            field=models.ForeignKey(default=1, to='taskManager.Notes'),
            preserve_default=True,
        ),
    ]
