# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0011_auto_20141120_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='componenttype',
            name='category',
            field=models.ForeignKey(to='electronics.ComponentCategory', null=True),
            preserve_default=True,
        ),
    ]
