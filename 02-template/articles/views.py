# import random
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


# def dinner(request):
#     foods = ['국밥', '국수', '카레', '탕수육',]
#     picked = random.choice(foods)
#     context = {}
#     return render(request, 'articles/dinner.html')


# def search(request):
#     return render(request, 'articles/search.html')


# def throw(request):
#     return render(request, 'articles/throw.html')


# def catch(request):
#     return render(request, 'articles/catch.html')
