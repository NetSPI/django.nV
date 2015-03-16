# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0019_notes_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=300, default='')),
                ('path', models.CharField(max_length=3000, default='')),
                ('project', models.ForeignKey(to='taskManager.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=200, default='N/A'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, default='N/A'),
            preserve_default=True,
        ),
    ]
