from django.shortcuts import render

# Create your views here.
def index(request):

    # DTL {{ name }}
    # name(key)의 bogum(value) 값을 가져온다.
    context = {
        'name' : 'bogum',
        'number' : 1
    }

    # render 함수의 3번째 항목, context(딕셔너리)
    return render(request, 'articles/index.html', context)

import random

def dinner(request):
    foods = ['족발', '보쌈', '치킨', '피자']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked
    }

    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # name = "throw"
    # GET : GET 방식
    # .get : 딕셔너리의 value
    # 'throw' : 딕셔너리의 key
    text = request.GET.get('throw')
    context = {
        'text' : text
    }
    return render(request, 'articles/catch.html', context)

def detail(request, number):

    context = {
        'number' : number
    }

    return render(request, 'articles/detail.html', context)