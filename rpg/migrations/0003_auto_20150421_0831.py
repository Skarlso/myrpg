# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0002_auto_20150421_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invetory',
            name='char_name',
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='Item', max_length=100),
        ),
    ]
