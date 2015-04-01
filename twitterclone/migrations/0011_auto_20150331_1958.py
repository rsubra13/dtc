# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitterclone', '0010_auto_20150331_1958'),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('message', models.TextField(max_length=1024)),
                ('created_date', models.DateTimeField()),
                ('photo_id', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=200)),
                ('userId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(to='twitterclone.Post'),
            preserve_default=True,
        ),
    ]
