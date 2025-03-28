from django.urls import path

# . : 현재 디렉토리
from . import views

# {% url namespace:name %}
# app_name = 'namespace'
app_name = 'articles'

urlpatterns = [
    # READ
    # 전체 게시글 조회
    path('', views.index, name = 'index'),
    # 단일 게시글 조회
    # variable routing <데이터타입:변수>
    path('<int:pk>/', views.detail, name = 'detail'),

    # CREATE
    # 렌더링(생성 페이지를 보여줄 거다)
    path('new/', views.new, name = 'new'),
    # 리다이렉트(생성 페이지를 눌렀을 때 게시글이 생성)
    path('create/', views.create, name = 'create'),

    # DELETE
    # 단일 게시글 조회 후 삭제
    # variable routing
    path('<int:pk>/delete/', views.delete, name='delete'),

    # UPDATE
    # 단일 게시글 조회 후 수정
    # variable routing
    # 페이지 렌더링
    path('<int:pk>/edit/', views.edit, name='edit'),
    # 페이지 리다이렉트
    path('<int:pk>/update/', views.update, name='update'),
]
