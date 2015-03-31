# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0004_auto_20150331_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='flickrid',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
