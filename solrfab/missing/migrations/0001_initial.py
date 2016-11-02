# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.BigIntegerField()),
                ('hair_color', models.CharField(max_length=255)),
                ('eye_color', models.CharField(max_length=255)),
                ('height', models.FloatField()),
                ('skin_color', models.CharField(max_length=255)),
                ('approximate_weight', models.FloatField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('approximate_number', models.BigIntegerField(null=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('image', models.ImageField(default='images/no-img.jpg', upload_to='images/')),
                ('cloutes', models.CharField(max_length=255, null=True)),
                ('reason', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_owner', to='user.UserProfiler')),
            ],
        ),
    ]