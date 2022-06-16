from django.db import connection
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.test.utils import CaptureQueriesContext
from django.db.models import Case,When,Count,Avg


from news.models import Article, CustomUser, UserArticleRelation
from news.serializers import ArticleSerializer

class ArticleApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='test_user')
        self.article_1 = Article.objects.create(title='Test article 1', author = self.user)
        self.article_2 = Article.objects.create(title='Test article 2', author = self.user)
        self.article_3 = Article.objects.create(title='Test article 3', author = self.user)

        UserArticleRelation.objects.create(user=self.user, article=self.article_1, like=True,rate=5)
        


    def test_get(self):
        url = reverse('article-list')
        with CaptureQueriesContext(connection) as queries:
            response = self.client.get(url)
            self.assertEqual(2, len(queries))
        articles = Article.objects.all().annotate(
            likes=Count(Case(When(userarticlerelation__like=True, then=1)))
        ).order_by('id')
        serializer_data = ArticleSerializer(articles, many=True).data
        self.assertEqual(status.HTTP_200_OK,response.status_code)
        self.assertEqual(serializer_data,response.data)
        self.assertEqual(serializer_data[0]['rating'], '5.00')
        self.assertEqual(serializer_data[0]['likes'], 1)
        
        