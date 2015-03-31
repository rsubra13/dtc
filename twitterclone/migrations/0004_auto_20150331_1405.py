# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0003_auto_20150331_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='postid',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='userid',
        ),
    ]
