# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('slug', models.SlugField(verbose_name='URL', editable=False)),
                ('menu', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0443\u043d\u043a\u0442\u0430 \u043c\u0435\u043d\u044e', blank=True)),
                ('ya_maps', models.TextField(help_text='\u0431\u0435\u0440\u0435\u0442\u0441\u044f \u0441 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440\u0430 \u043a\u0430\u0440\u0442 \u0442\u0443\u0442 http://api.yandex.ru/maps/tools/constructor/ \t\t\t\t\t\t\t\u0422\u0430\u043a \u0436\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432 \u0440\u0443\u0447\u043d\u0443\u044e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440\u044b \u043a\u0430\u0440\u0442\u044b width=825&height=350', null=True, verbose_name='\u042f\u043d\u0434\u0435\u043a\u0441 \u043a\u0430\u0440\u0442\u0430 ', blank=True)),
                ('subline', models.TextField(help_text='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0433\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c', blank=True)),
                ('index', models.IntegerField(help_text='\u0412 \u043f\u043e\u043b\u0435 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f', verbose_name='\u0418\u043d\u0434\u0435\u043a\u0441')),
                ('region', models.CharField(help_text='\u0412\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440:\t\t\t\t\t\t\t\u0421\u0432\u0435\u0440\u0434\u043b\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c, \u0438\u043b\u0438 \u042f\u043c\u0430\u043b\u043e-\u041d\u0435\u043d\u0435\u0446\u043a\u0438\u0439 \u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433', max_length=255, null=True, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c/\u041a\u0440\u0430\u0439/\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433', blank=True)),
                ('city', models.CharField(help_text="\u0412\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \t\t\t\t\t\t\t'\u0433\u043e\u0440\u043e\u0434 \u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433', \u0438\u043b\u0438 '\u043f\u043e\u0441\u0435\u043b\u043e\u043a \u0412\u0435\u0441\u0435\u043b\u043e\u0432\u043a\u0430'", max_length=255, null=True, verbose_name='\u0413\u043e\u0440\u043e\u0434', blank=True)),
                ('street', models.CharField(help_text="\u0412\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \t\t\t\t\t\t\t'\u0443\u043b\u0438\u0446\u0430 \u041b\u0435\u043d\u0438\u043d\u0430', \u0438\u043b\u0438 '\u043f\u043b\u043e\u0449\u0430\u0434\u044c \u0412\u043e\u0441\u0441\u0442\u0430\u043d\u0438\u044f'", max_length=255, null=True, verbose_name='\u0423\u043b\u0438\u0446\u0430', blank=True)),
                ('building', models.CharField(help_text="\u0412\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: '\u0434\u043e\u043c 13', \u0438\u043b\u0438 '\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 5, \u043a\u043e\u0440\u043f\u0443\u0441 '\u0430''", max_length=255, null=True, verbose_name='\u0414\u043e\u043c/\u0421\u0442\u0440\u043e\u0435\u043d\u0438\u0435', blank=True)),
                ('office', models.CharField(help_text="\u0415\u0441\u043b\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u043c \u043f\u0443\u0441\u0442\u044b\u043c.\t\t\t\t\t\t\t\u0412\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: '\u043e\u0444\u0438\u0441 13', \u0438\u043b\u0438 '\u043a\u0432\u0430\u0440\u0442\u0438\u0440\u0430 10'", max_length=255, null=True, verbose_name='\u041e\u0444\u0438\u0441', blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='\u041f\u043e\u0447\u0442\u0430', blank=True)),
                ('subline', models.CharField(max_length=255, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c \u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c', blank=True)),
                ('contact', models.ForeignKey(related_name=b'contact_email', to='contacts.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', blank=True)),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name=b'E-mail')),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('body', models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactPhone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('subline', models.CharField(max_length=255, null=True, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c \u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c', blank=True)),
                ('contact', models.ForeignKey(related_name=b'contact_phones', to='contacts.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('working_time', models.CharField(max_length=255, null=True, verbose_name='\u0414\u043d\u0438 \u043d\u0435\u0434\u0435\u043b\u0438', blank=True)),
                ('working_time_eng', models.CharField(help_text='\u0434\u043d\u0438 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0434\u0432\u0443\u0445\u0431\u0443\u043a\u0432\u0435\u043d\u043d\u044b\u043c\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f\u043c\u0438: Mo, Tu, We, Th, Fr, Sa, Su;\t\t\t\t\t\t\t\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: Mo - Su, \u0438\u043b\u0438 \u043f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435\u043c Mo,Tu,We,Th', max_length=255, null=True, verbose_name='\u0414\u043d\u0438 \u043d\u0435\u0434\u0435\u043b\u0438 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c', blank=True)),
                ('value', models.CharField(help_text='\u0432\u0440\u0435\u043c\u044f \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0432 24-\u0447\u0430\u0441\u043e\u0432\u043e\u043c \u0444\u043e\u0440\u043c\u0430\u0442\u0435. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 15:00 - 20:00', max_length=255, null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True)),
                ('contact', models.ForeignKey(related_name=b'working_time', to='contacts.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
