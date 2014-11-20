# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0010_auto_20141120_0704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(max_length=500)),
                ('shipping_num', models.CharField(max_length=20, blank=True)),
                ('supplier', models.CharField(max_length=100, blank=True)),
                ('notes', models.TextField(default=b'', blank=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(blank=True)),
                ('component', models.ForeignKey(to='electronics.Component')),
                ('order', models.ForeignKey(to='electronics.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField(default=b'', blank=True)),
                ('component', models.ForeignKey(to='electronics.Component')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='component',
            name='notes',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='componenttype',
            name='notes',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parameter',
            name='notes',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='notes',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
