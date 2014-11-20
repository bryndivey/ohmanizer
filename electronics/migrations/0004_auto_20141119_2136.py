# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0003_stock_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentParameterValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=10)),
                ('component', models.ForeignKey(to='electronics.Component')),
                ('parameter', models.ForeignKey(to='electronics.Parameter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='componenttype',
            name='parameters',
            field=models.ManyToManyField(to='electronics.Parameter'),
            preserve_default=True,
        ),
    ]
