# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0005_photo_flickrid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_id',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
