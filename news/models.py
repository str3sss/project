import re
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=False, null=False)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    

class Article(models.Model):
    title = models.CharField(verbose_name='Название',max_length=50,blank=False)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='articles')

    readers = models.ManyToManyField(CustomUser, through='UserArticleRelation',related_name='rate_articles')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f'{self.title} by {self.author}'



class UserArticleRelation(models.Model):
    RATE_CHOICES = (
        (-1,-1),    
        (0,0),
        (1,1)
    )

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    rate = models.SmallIntegerField(choices=RATE_CHOICES,default=0)
    like = models.BooleanField(default=False)
    in_bookmark = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} rate:   {self.article}'