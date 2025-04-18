from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

<<<<<<< HEAD
# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 데이터 조회
    if request.method == 'GET':
=======

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 데이터 조회
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
        articles = Article.objects.all()
        # articles는 django에서는 쓸 수 있는 queryset 데이터 타입이기 때문에
        # 우리가 만든 모델시리얼라이저로 변환 진행
        serializer = ArticleListSerializer(articles, many=True)
        # DRF에서 제공하는 Response를 사용해 JSON 데이터를 응답
        # JSON 데이터는 serializer의 data 속성에 존재
        return Response(serializer.data)

    # 게시글 생성 요청에 대한 응답
    elif request.method == 'POST':
        # 예전 코드
<<<<<<< HEAD
        # form = ArticleForm(request.POST)
        # 사용자 입력 데이터를 클래스로 받아서 반환
        serializer = ArticleSerializer(data=request.data)
        #유효성 검사
=======
        # form = ArticleFrom(request.POST)
        # 사용자가 보낸 ㅈ데이터를 클래스로 받아서 직렬화
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
=======


>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 단일 게시글 데이터 조회
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # ArticleSerializer 클래스로 직렬화를 진행
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
<<<<<<< HEAD
        # 사용자가 보낸 수정 데이터를 변환
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=statis.HTTP_400_BAD_REQUEST)
=======
        # 사용자가 보낸 수정 데이터를 직렬화
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
