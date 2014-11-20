# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0005_parameter_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='description',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
