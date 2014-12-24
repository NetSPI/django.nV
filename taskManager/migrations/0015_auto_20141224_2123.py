# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0014_auto_20141224_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='users_assinged',
            new_name='users_assigned',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='users_assinged',
            new_name='users_assigned',
        ),
    ]
