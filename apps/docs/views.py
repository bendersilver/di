# -*- coding: utf-8 -*-
from django.db.models import get_model
from django.views.generic import ListView

DocsTitle = get_model('docs', 'DocsTitle')

class DocsListView(ListView):
    context_object_name = 'objs'
    model = DocsTitle
    template_name = 'docs/list.html'

    def get_context_data(self, **kwargs):
        context = super(DocsListView, self).get_context_data(**kwargs)
        context['title'] = u'Документы'
        return context