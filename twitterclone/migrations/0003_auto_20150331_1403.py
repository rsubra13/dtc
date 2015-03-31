# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0002_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='flickrid',
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
