from django.test import TestCase
from django.urls import reverse
from .models import Article
# Create your tests here.

class ArticlesTest(TestCase):
    fixtures = ["article.json"]

    def test_articles_list(self):
        response = self.client.get(reverse('articles:index'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('articles', response.context)

        articles = response.context['articles']
        self.assertTrue(len(articles) > 0)

    def test_update_article(self):
        update_url = reverse('articles:update', kwargs={'article_id': 1})
        index_url = reverse('articles:index')

        initial = Article.objects.get(id=1)
        self.client.post(update_url, {
            'name': 'test_success',
            'csrfmiddlewaretoken': 'testtoken'
        })

        response = self.client.get(index_url)
        self.assertContains(response, 'test_success')
        self.assertNotContains(response, initial)