# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0012_auto_20141121_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='datasheet',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
