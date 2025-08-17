from django.urls import path
from .views import (
    home, register, profile, 
    UserLoginView, UserLogoutView, 
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, 
    CommentCreateView, CommentUpdateView, CommentDeleteView, 
    PostByTagListView, SearchResultsView
)

urlpatterns = [
    # Main
    path("", home, name="home"),
    path("search/", SearchResultsView.as_view(), name="search"),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),

    # Posts
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comments
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="update-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),

    # Auth
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]