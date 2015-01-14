# -*- coding: utf-8 -*-
from django.db.models import get_model
from django.views.generic import ListView


Gallery = get_model('home', 'Gallery')


class HomePageView(ListView):
    context_object_name = 'objs'
    model = Gallery
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomePageView, self).get_context_data(**kwargs)
        return ctx