from django.db import models

# Create your models here.
class Board(models.Model):
    # 제목은 글자 제한을 20글자
    # 왜 게시글의 제목은 글자 제한을 둬야 할까?
    title = models.CharField(max_length=20)
    # 게시글 내용(글자 제한 x)
    content = models.TextField()
    # auto_now_add : 객체가 처음 생성될 때 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 객체가 저장될 때의 현재 시간
    updated_at = models.DateTimeField(auto_now=True)
    # 수동 입력 시간
    # time_at = models.DateTimeField(null=True, blank=True)