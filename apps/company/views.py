# -*- coding: utf-8 -*-
from django.db.models import get_model
from django.views.generic import ListView, DetailView


Company = get_model('company', 'Company')

class CompanListView(ListView):
    context_object_name = 'objs'
    model = Company

    def get(self, request, *args, **kwargs):
    	self.pages = self.model.objects.all().count()
        return super(CompanListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
    	if self.pages == 1:
    		self.context_object_name = 'obj'
    		return self.model.objects.all()[0]
    	else:
    		return super(CompanListView, self).get_queryset()

    def get_template_names(self):
    	if self.pages == 1:
    		return ['company/detail.html']
    	else:
    		return ['company/list.html']

class CompanDetailView(DetailView):
    context_object_name = 'obj'
    model = Company
    template_name = 'company/detail.html'