# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-29 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20180429_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_provider', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('street', models.CharField(max_length=64)),
                ('number_street', models.IntegerField()),
            ],
            options={
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_supply', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Catalog')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Provider')),
            ],
            options={
                'db_table': 'supply',
            },
        ),
    ]
