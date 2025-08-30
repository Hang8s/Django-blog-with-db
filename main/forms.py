from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PostModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
        
class AddPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','text']
    