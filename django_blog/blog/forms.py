from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget


# User Creation Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Post Form
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(),
        }


# Comment Form
class CommentForm(forms.ModelForm):
    content = forms.CharField(   # <<< ضفناها كـ explicit
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment..."}),
        max_length=500,
        required=True,
        help_text="Enter your comment here."
    )

    class Meta:
        model = Comment
        fields = ["content"]