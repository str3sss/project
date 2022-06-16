from pyexpat import native_encoding
from django.urls import path
from .views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(),name='article-list')
]
