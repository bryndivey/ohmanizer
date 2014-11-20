# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='designation',
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(default=b'', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='subslot',
            field=models.CharField(default='', max_length=40, blank=True),
            preserve_default=False,
        ),
    ]
