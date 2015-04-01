# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0006_auto_20150331_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
        migrations.AddField(
            model_name='photo',
            name='url',
            field=models.URLField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
