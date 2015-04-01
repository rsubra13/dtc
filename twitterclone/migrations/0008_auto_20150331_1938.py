# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0007_auto_20150331_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='post',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
