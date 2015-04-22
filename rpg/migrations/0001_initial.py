# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CommaSeparatedIntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Item', max_length=100)),
                ('damage', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('consumable', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ForeignKey(to='rpg.Inventory'),
        ),
        migrations.AddField(
            model_name='character',
            name='user_id',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
