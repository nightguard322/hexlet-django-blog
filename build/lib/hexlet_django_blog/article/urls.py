from django.urls import path
from django.shortcuts import redirect

from hexlet_django_blog.article import views
from .views import ArticleView

urlpatterns = [
    path(
        'tags/<int:article_id>/',
        ArticleView.as_view(template_name='article/index.html'),
        name='article'
        ),
]