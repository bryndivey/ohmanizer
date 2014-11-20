# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0009_auto_20141120_0703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['designation']},
        ),
        migrations.AlterModelOptions(
            name='parameter',
            options={'ordering': ['name']},
        ),
    ]
