from django.urls import path
from django.shortcuts import redirect

from hexlet_django_blog.article import views

app_name = 'articles'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:article_id>/edit/', views.ArticleFormEditView.as_view(), name='update'),
    path('<int:article_id>/delete/', views.ArticleFormDeleteView.as_view(), name='delete'),
    path('<int:article_id>/', views.ArticleView.as_view(), name='show'),
    path('create/', views.CreateArticleView.as_view(), name='create')
]