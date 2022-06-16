from django.utils import timezone
from django.views.generic import ListView,DetailView
from django.shortcuts import render
from news.models import Article, UserArticleRelation
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from news.serializers import ArticleSerializer, UserArticleRelationSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin
from rest_framework.permissions import  IsAuthenticated
from django.db.models import Count,Avg
from django.db.models.expressions import Case,When



class ArticleListView(ListView):
    model = Article

    queryset = Article.objects.all().annotate(
        likes=Count(Case(When(userarticlerelation__like=True, then=1))),
        rating=Avg('userarticlerelation__rate'),
    ).order_by('id')

    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
    
class ArticleDetail(DetailView):
    model=Article
    context_object_name='artcile'
    template_name = 'news/article_detail.html'
    

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all().annotate(
        likes=Count(Case(When(userarticlerelation__like=True, then=1))),
        rating=Avg('userarticlerelation__rate'),
    ).select_related('author').order_by('id')

    serializer_class = ArticleSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filter_fields = ['id']
    search_fields = ['title']
    ordering_fields = ['created']


class UserArticleRelationViewSet(RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserArticleRelation.objects.all()
    serializer_class = UserArticleRelationSerializer
    lookup_field = 'article'

    def get_object(self):
        obj, created =UserArticleRelation.objects.get_or_create(user=self.request.user,
                                                          article_id=self.kwargs['article'])
        return obj


def rateArtcile(request):
    if request.method == "POST":
        form = RatingForm
        if form.is_valid():
            pass