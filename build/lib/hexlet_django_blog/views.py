from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article'), kwargs={id: 42})

class AboutView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = "Example"
        return context