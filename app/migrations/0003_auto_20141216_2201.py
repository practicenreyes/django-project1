# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_enlace_categroria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enlace',
            old_name='categroria',
            new_name='categoria',
        ),
    ]
