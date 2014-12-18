# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlace',
            name='categroria',
            field=models.ForeignKey(to='app.Categoria', default=0),
            preserve_default=False,
        ),
    ]
