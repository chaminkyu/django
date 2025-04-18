<<<<<<< HEAD
from rest_framework import serializers
from .models import Article


# 게시글의 일부 필드를 직렬화하는 클래스
=======
from rest_framework import serializers 
from .models import Article


# 게시글의 일부 필드를 직렬화 하는 클래스
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

<<<<<<< HEAD
# 게시글의 전체 필드를 직렬화하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):
=======

# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
    class Meta:
        model = Article
        fields = '__all__'