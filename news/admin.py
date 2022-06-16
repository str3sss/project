from django.contrib import admin
from news.models import Article, CustomUser, UserArticleRelation

admin.site.register(CustomUser)
admin.site.register(Article)
admin.site.register(UserArticleRelation)
