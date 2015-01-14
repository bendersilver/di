from apps.contacts.models import *
from django.contrib import admin

class WorkingTimeInline(admin.TabularInline):
	model = WorkingTime
	extra = 1

class ContactPhoneInline(admin.TabularInline):
	model = ContactPhone
	extra = 1

class ContactEmailInline(admin.TabularInline):
	model = ContactEmail
	extra = 1

class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,              {'fields': ['title',
						        'subline',
						        'ya_maps',
						        'menu',]}),

        ('Address',			{'fields': ['index', 'region', 'city', 'street', 'building', 'office'], 'classes': ['collapse']}),

    ]
	inlines = [WorkingTimeInline,
			ContactPhoneInline,
			ContactEmailInline,
			]



admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactForm)