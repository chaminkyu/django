<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # model = User
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', )
=======
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
