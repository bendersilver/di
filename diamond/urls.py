from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.home.views import HomePageView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
	url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^company/', include('apps.company.urls')),
    url(r'^document/', include('apps.docs.urls')),
    url(r'^contacts/', include('apps.contacts.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
