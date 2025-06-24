from django.urls import path
from django.views.generic import TemplateView

from hexlet_django_blog.article import views
from .views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view(template_name='article/index.html'))
]