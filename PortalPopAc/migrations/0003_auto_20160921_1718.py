# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortalPopAc', '0002_auto_20160921_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bo',
            name='impacto',
            field=models.CharField(choices=[('x', 'Muito baixo'), ('xx', 'Baixo'), ('xxx', 'M\xe9dio'), ('xxxx', 'Alto'), ('xxxxxx', 'Muito alto')], default='x', max_length=5, verbose_name='Impacto'),
        ),
    ]
