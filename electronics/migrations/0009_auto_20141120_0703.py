# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0008_auto_20141120_0643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componenttype',
            options={'ordering': ['name']},
        ),
    ]
