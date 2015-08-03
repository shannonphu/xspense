# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_xspense', '0003_budget_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
    ]
