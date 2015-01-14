# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430')),
                ('fi', models.FileField(upload_to=b'docs/%Y/%m/', verbose_name='\u0424\u0430\u0439\u043b')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocsTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0433\u0440\u0443\u043f\u043f\u044b')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='docs',
            name='doc',
            field=models.ForeignKey(to='docs.DocsTitle'),
            preserve_default=True,
        ),
    ]
