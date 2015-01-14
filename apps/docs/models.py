# -*- coding: utf-8 -*-
import uuid

from django.db import models

class DocsTitle(models.Model):
	title = models.CharField(max_length=255,
							verbose_name=u'Заголовок группы')

	def __unicode__(self):
		return u"%s" % self.title

	class Meta:
		verbose_name = u'Документы'
        verbose_name_plural = u'Документы'

class Docs(models.Model):

	def content_file_name(instance, filename):
		filename = str(uuid.uuid1()) + '.' + filename.split('.')[-1]
		return ('docs/' + filename)

	doc = models.ForeignKey('DocsTitle', related_name='documents')
	title = models.CharField(max_length=255,
							verbose_name=u'Название файла')
	fi = models.FileField(upload_to=content_file_name,
							verbose_name=u'Файл')

	def __unicode__(self):
		return u"%s" % self.title

	class Meta:
		verbose_name = u'Документы'
		verbose_name_plural = u'Документы'

	def get_file_format(self):
		return self.fi.name.split('.')[-1]