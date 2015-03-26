# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('message', models.CharField(max_length=1024)),
                ('created_date', models.DateTimeField()),
                ('photo_id', models.CharField(unique=True, max_length=50)),
                ('tags', models.CharField(max_length=200)),
                ('userId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
