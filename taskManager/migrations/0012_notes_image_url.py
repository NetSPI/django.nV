# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0011_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='image_url',
            field=models.CharField(max_length=200, default=datetime.date(2014, 12, 12)),
            preserve_default=False,
        ),
    ]
