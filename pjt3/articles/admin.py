from django.contrib import admin

# models.py로부터 Board 클래스
# . : 현재 디렉토리리
from .models import Board

# admin site에 등록
admin.site.register(Board)