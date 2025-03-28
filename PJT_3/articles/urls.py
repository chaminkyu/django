from django.urls import path

# . : 현재 디렉토리
from . import views

# {% url namespace:name %}
# app_name = 'namespace'
app_name = 'articles'

urlpatterns = [
    # 전체 게시글 조회
    path('index/', views.index, name = 'index'),
]