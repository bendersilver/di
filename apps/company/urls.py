from django.conf.urls import patterns, include, url
from apps.company.views import CompanListView, CompanDetailView

urlpatterns = patterns('',
    url(r'^$', CompanListView.as_view(), name='company_index'),
    url(r'^(?P<slug>[\w-]*)-(?P<pk>\d+)/$',
                 CompanDetailView.as_view(), name='company_detail'),
)
