# -*- coding: utf-8 -*-
from django.db import models


class Gallery(models.Model):
	title = models.CharField(u"Заголовок", max_length=255)
	subline = models.TextField(u'Текст',
				blank=True, null=True)
	img = models.ImageField(u'Изображение',
				upload_to='photos/base/%Y/%m/%d',
				blank=True, null=True)


	def __unicode__(self):
		return u"%s" % self.title

	class Meta:
		verbose_name = u'Галерея'
        verbose_name_plural = u'Галерея'