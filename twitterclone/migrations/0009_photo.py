# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0008_auto_20150331_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.URLField(max_length=255, blank=True)),
                ('server', models.CharField(max_length=255, blank=True)),
                ('farm', models.CharField(max_length=255, blank=True)),
                ('secret', models.CharField(max_length=255, blank=True)),
                ('flickrid', models.CharField(max_length=255, blank=True)),
                ('post', models.ForeignKey(to='twitterclone.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
