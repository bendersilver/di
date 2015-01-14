# -*- coding: utf-8 -*-
from django.db import models

class Contact(models.Model):
	title = models.CharField(max_length=255,
							verbose_name=u'Заголовок')
	slug = models.SlugField(editable=False,
							verbose_name=u"URL")
	menu = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Название пункта меню')
	ya_maps = models.TextField(blank=True, null=True,
							verbose_name=u"Яндекс карта ",
							help_text=u"берется с конструктора карт тут http://api.yandex.ru/maps/tools/constructor/ \
							Так же необходимо в ручную указать размеры карты width=825&height=350")
	subline = models.TextField(blank=True, null=True,
							verbose_name=u"Текст под заголовком",
							help_text=u"Краткое описание содержимого страницы")
	index = models.IntegerField(
							verbose_name=u'Индекс',
							help_text=u"В поле поддерживаются только числовые значения")
	region = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Область/Край/Автономный округ',
							help_text=u"Вписывается значение полностью. Например:\
							Свердловская область, или Ямало-Ненецкий автономный округ")
	city = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Город',
							help_text=u"Вписывается значение полностью. Например: \
							'город Екатеринбург', или 'поселок Веселовка'")
	street = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Улица',
							help_text=u"Вписывается значение полностью. Например: \
							'улица Ленина', или 'площадь Восстания'")
	building = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Дом/Строение',
							help_text=u"Вписывается значение полностью. Например: 'дом 13', или 'строение 5, корпус 'а''")
	office = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Офис',
							help_text=u"Если значение отсутствует оставляем пустым.\
							Вписывается значение полностью. Например: 'офис 13', или 'квартира 10'")

	def __unicode__(self):
		return u"%s" % self.title


	class Meta:
		verbose_name = u'Контакты'
		verbose_name_plural = u'Контакты'


class WorkingTime(models.Model):
	contact = models.ForeignKey('Contact', related_name='working_time')
	working_time = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Дни недели')
	working_time_eng = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Дни недели на английском',
							help_text=u"дни указываются двухбуквенными комбинациями: Mo, Tu, We, Th, Fr, Sa, Su;\
							Например: Mo - Su, или перечислением Mo,Tu,We,Th")
	value = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Время работы',
							help_text=u"время указывается в 24-часовом формате. Например, 15:00 - 20:00")

class ContactPhone(models.Model):
	contact = models.ForeignKey('Contact', related_name='contact_phones')
	phone = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Телефон')
	subline = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Подпись если есть')

class ContactEmail(models.Model):
	contact = models.ForeignKey('Contact', related_name='contact_email')
	email = models.EmailField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Почта')
	subline = models.CharField(blank=True,
							max_length=255,
							verbose_name=u'Подпись если есть')


class ContactForm(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
	phone = models.CharField(blank=True, null=True,
							max_length=255,
							verbose_name=u'Телефон')
	email = models.EmailField(verbose_name='E-mail')
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	body = models.TextField(verbose_name='Сообщение')
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = u'Контактная форма'
		verbose_name_plural = u'Контактная форма'


	def __unicode__(self):
		return self.title
