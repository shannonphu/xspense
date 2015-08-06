# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_xspense', '0005_expense_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.IntegerField(choices=[(0, 'electronics'), (1, 'office'), (2, 'entertainment'), (3, 'home/furniture'), (4, 'clothes'), (5, 'baby/kids'), (6, 'toys/games/crafts'), (7, 'food'), (8, 'health'), (9, 'beauty'), (10, 'sports/fitness'), (11, 'auto'), (12, 'gifts'), (13, 'other'), (14, 'education')], default=13),
        ),
    ]
