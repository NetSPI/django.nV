# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskManager', '0002_auto_20141010_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('comment_text', models.CharField(max_length=200)),
                ('task', models.ForeignKey(to='taskManager.Task')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='task',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
