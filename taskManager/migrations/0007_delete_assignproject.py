# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0006_auto_20141209_0644'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssignProject',
        ),
    ]
