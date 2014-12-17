# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0010_auto_20141211_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.CharField(max_length=200, default='ancestor'),
            preserve_default=True,
        ),
    ]
