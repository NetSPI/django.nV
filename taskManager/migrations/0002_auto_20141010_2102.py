# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='project',
            name='project_title',
            field=models.CharField(default='Default', max_length=50),
            preserve_default=True,
        ),
    ]
