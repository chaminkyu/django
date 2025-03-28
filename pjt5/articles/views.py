from django.shortcuts import render, redirect

# 현재 디렉토리의 models.py로 부터 Board 모델을 가져오겠다. 
from .models import Article

def index(request):
    # QuerySetAPI ---> Read, 전체 데이터 조회 : Board.objects.all()
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # QuerySet API : 단일 데이터 조회 : get
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1번방법, 2번방법, 3번방법(3번 방법은 지양)
    # save()하기전에 유효성검사를 해야한다
    # form태그의 name으로 조회

    # GET 방식 : url에 노출 --- 데이터 조회, 검색
    # POST 방식 : url에 노출 x(보안성) --- 데이터 생성, 수정, 삭제
    # POST방식이 짱이지만 GET방식을 쓰는 이유
    # GET방식에 비해 POST방식 훨씬 복잡하다. : ex) (csrf토큰) - (보안토큰)

    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2벙 방법(안정성, 코드간결)
    article = Article(title = title, content = content)
    # 데이터를 DB에 함부로 저장하면 안된다..
    # save하기전에 유효성 검사
    article.save()

    # render, redirect 차이
    # 우리가 사용자에게 새로운 페이지를 보여줄때 사용(렌더링) : render
    # 데이터 처리 후(생성, 수정, 삭제) 다른 페이지로 이동 할때 : redirect
    return redirect('articles:detail', article.pk)


# 단일 게시글 조회 후 삭제
def delete(request, pk):
    # QuerySetAPI
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

# 페이지 렌더링(게시글 조회)
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

# 페이지 리다이렉트(create와 차이 : 기존에 있던 게시글을 변경)
def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    article.save()

    # 데이터가 변경되었으니 render아니라 redirect
    return redirect('articles:detail', article.pk)