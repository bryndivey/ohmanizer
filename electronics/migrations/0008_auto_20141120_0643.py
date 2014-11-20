# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0007_stock_last_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componenttype',
            name='parameters',
            field=models.ManyToManyField(to='electronics.Parameter', blank=True),
            preserve_default=True,
        ),
    ]
