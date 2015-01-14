from django.conf.urls import patterns, include, url
from apps.contacts.views import ContactListView, ContactDetailView, ContactFormView

urlpatterns = patterns('',
    url(r'^$', ContactListView.as_view(), name='contact_index'),
    url(r'^(?P<slug>[\w-]*)-(?P<pk>\d+)/$',
                 ContactDetailView.as_view(), name='contact_detail'),
    url(r'^send_request/$', ContactFormView.as_view(), name='contact_form'),
)
