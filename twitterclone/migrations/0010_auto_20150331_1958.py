# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0009_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='post',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='userId',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
