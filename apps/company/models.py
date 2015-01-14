# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Company(models.Model):
	title = models.CharField(max_length=255,
							verbose_name=u'Заголовок')
	slug = models.SlugField(verbose_name=u"URL", editable=False)
	menu = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Название пункта меню')
	subline = RichTextField(u"Текст страницы")

	def __unicode__(self):
		return u"%s" % self.title

	class Meta:
		verbose_name = u'Компания'
        verbose_name_plural = u'Компания'