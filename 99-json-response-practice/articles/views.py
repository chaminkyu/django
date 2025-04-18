<<<<<<< HEAD
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(['GET'])
@api_view()
def article_json(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
=======
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(['GET'])
@api_view()
def article_json(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
