# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='user_id',
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='items',
        ),
        migrations.AddField(
            model_name='inventory',
            name='items',
            field=models.ManyToManyField(to='rpg.Item'),
        ),
    ]
