from rest_framework.serializers import ModelSerializer,SerializerMethodField,IntegerField,DecimalField,CharField

from .models import Article, UserArticleRelation

class ArticleSerializer(ModelSerializer):
    # likes_count = SerializerMethodField()
    likes = IntegerField(read_only=True)
    rating  = DecimalField(max_digits=3,decimal_places=2,read_only=True)
    author_name = CharField(source='author.username',default='',read_only=True)
    
    class Meta:
        model = Article
        fields = ['id','title','author_name','created','updated','likes','rating']

    # def get_likes_count(self,instance):
    #     return UserArticleRelation.objects.filter(article=instance, like=True).count()

        

class UserArticleRelationSerializer(ModelSerializer):
    class Meta:
        model = UserArticleRelation
        fields = ['article','like','in_bookmark','rate']