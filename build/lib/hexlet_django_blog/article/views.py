from django.shortcuts import render
from django.http import HttpResponse
import os
from django.views.generic import TemplateView
# Create your views here.

class ArticleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = kwargs.get('article_id')
        context['article_id'] = article_id
        return context