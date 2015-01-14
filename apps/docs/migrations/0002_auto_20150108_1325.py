# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docs',
            options={'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b', 'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='docs',
            name='doc',
            field=models.ForeignKey(related_name=b'documents', to='docs.DocsTitle'),
        ),
    ]
