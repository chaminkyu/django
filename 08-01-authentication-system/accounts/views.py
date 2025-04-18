from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # auth_login(request, 로그인 인증된 유저 객체)
            auth_login(request, form.get_user())
            return redirect('articles:index')
<<<<<<< HEAD

=======
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

<<<<<<< HEAD
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
=======

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
