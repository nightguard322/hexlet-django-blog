from django.shortcuts import render
from django.http import HttpResponse
import os
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Article
from django.views import View
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.messages import get_messages
# Create your views here.


class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()
        messages = get_messages(request)
        return render(
        request,
        'article/index.html',
        context = {
            'articles': articles,
            'messages': messages
            })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs['id']
        article = get_object_or_404(Article, pk=article_id)
        return render(
            request,
            'article/show.html',
            context = {'article': article})


class CreateArticleView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully added.")
            return redirect('articles:index')
        return render(
        request,
        'article/show.html',
        context = {'article': form})
            

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'article/create.html',
            context = {'form': form})

class ArticleFormEditView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs['article_id']
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully added.")
            return redirect('articles:index')
        return render(
            request,
            'article/update.html',
            context = {
                'form': form,
                'article_id': article_id
            })
            

    def get(self, request, *args, **kwargs):
        article_id = kwargs['article_id']
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            'article/update.html',
            context = {
                'form': form,
                'article_id': article_id
            })


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs['article_id']
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles:index')