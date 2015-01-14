from django.contrib import admin
from apps.docs.models import DocsTitle, Docs

class DocsInline(admin.TabularInline):
    model = Docs

class DocsTitleAdmin(admin.ModelAdmin):
    inlines = [
        DocsInline,
    ]

admin.site.register(DocsTitle, DocsTitleAdmin)