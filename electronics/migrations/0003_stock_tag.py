# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import electronics.models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0002_auto_20141119_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='tag',
            field=models.CharField(default=electronics.models.random_tag, max_length=5),
            preserve_default=True,
        ),
    ]
