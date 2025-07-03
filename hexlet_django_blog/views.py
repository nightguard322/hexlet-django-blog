from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .article.models import Article

class IndexView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = "Example"
        return context

class AboutView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = "Example"
        return context

