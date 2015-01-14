# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('slug', models.SlugField(verbose_name='URL', editable=False)),
                ('menu', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0443\u043d\u043a\u0442\u0430 \u043c\u0435\u043d\u044e', blank=True)),
                ('subline', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
    ]
