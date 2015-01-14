from django.conf.urls import patterns, include, url
from apps.docs.views import DocsListView

urlpatterns = patterns('',
    url(r'^$', DocsListView.as_view(), name='doc_index'),
)
