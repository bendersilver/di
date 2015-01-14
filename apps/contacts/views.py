# -*- coding: utf-8 -*-
from django.db.models import get_model
from django.views.generic import ListView, DetailView, View
from django.http import Http404, HttpResponse


Contact = get_model('contacts', 'Contact')
ContactForm = get_model('contacts', 'ContactForm')

class ContactListView(ListView):
    context_object_name = 'objs'
    model = Contact

    def get(self, request, *args, **kwargs):
    	self.pages = self.model.objects.all().count()
        return super(ContactListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
    	if self.pages == 1:
    		self.context_object_name = 'obj'
    		return self.model.objects.all()[0]
    	else:
    		return super(ContactListView, self).get_queryset()

    def get_template_names(self):
    	if self.pages == 1:
    		return ['contacts/detail.html']
    	else:
    		return ['contacts/list.html']

class ContactDetailView(DetailView):
    context_object_name = 'obj'
    model = Contact
    template_name = 'contacts/detail.html'


class ContactFormView(View):

    def get(self, request, *args, **kwargs):
    	raise Http404

    def post(self, request, *args, **kwargs):
    	m = ContactForm()
    	for k, v in request.POST.items():
    		if k == 'date':
    			dd, mm, yy = str(v).split('.')
    			v = yy + '-' + mm  + '-' + dd
    		setattr(m, k, v)
    	m.save()
    	return HttpResponse('ok')
