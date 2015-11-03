# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 3, 16, 20, 37, 589549)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='funny',
            field=models.BooleanField(default=False),
        ),
    ]
