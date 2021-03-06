# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-24 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='heroinfo',
            options={'verbose_name': '英雄', 'verbose_name_plural': '英雄'},
        ),
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
                ('books', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='booktest', verbose_name='图片'),
        ),
    ]
