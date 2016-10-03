# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('isadmin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=75, null=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
                ('adminid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('assignedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='By', to='Team.Member')),
                ('assignedto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To', to='Team.Member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='projectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Team.Project'),
        ),
        migrations.AddField(
            model_name='member',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.User'),
        ),
    ]