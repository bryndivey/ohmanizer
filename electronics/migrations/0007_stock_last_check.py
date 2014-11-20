# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0006_auto_20141119_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='last_check',
            field=models.DateField(default=datetime.datetime.utcnow),
            preserve_default=True,
        ),
    ]
