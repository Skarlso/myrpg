# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('char_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invetory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('char_name', models.CharField(max_length=100)),
                ('items', models.CommaSeparatedIntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('damage', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('consumable', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ForeignKey(to='rpg.Invetory'),
        ),
    ]
