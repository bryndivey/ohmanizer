# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0004_auto_20141119_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='description',
            field=models.CharField(default='', max_length=40, blank=True),
            preserve_default=False,
        ),
    ]
