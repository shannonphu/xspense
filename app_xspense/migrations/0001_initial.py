# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category', models.IntegerField(choices=[(0, 'electronics'), (1, 'office'), (2, 'entertainment'), (3, 'home/furniture'), (4, 'clothes'), (5, 'baby/kids'), (6, 'toys/games/crafts'), (7, 'food'), (8, 'health'), (9, 'beauty'), (10, 'sports/fitness'), (11, 'auto'), (12, 'gifts'), (13, 'other')], default=13)),
                ('purpose', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('item', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.TextField()),
                ('budget', models.ForeignKey(to='app_xspense.Budget')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
