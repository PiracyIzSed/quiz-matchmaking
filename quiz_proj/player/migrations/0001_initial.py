# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-03 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile_no', models.BigIntegerField()),
                ('country_code', models.CharField(default='+91', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='question.Category')),
                ('player', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.Player')),
            ],
        ),
    ]
