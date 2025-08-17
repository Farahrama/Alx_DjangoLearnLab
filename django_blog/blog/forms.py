from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget


# Form for new users
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Form for blog posts
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Separate with commas")

    class Meta:
        model = Post
        fields = ["post_title", "body", "tags"]  # adjusted names from models.py
        widgets = {
            "tags": TagWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]