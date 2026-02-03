
from .views import PostListCreateAPIView, CommentListCreateAPIView
from django.urls import path

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="posts" ),
    path(  "posts/<int:post_id>/comments/",
        CommentListCreateAPIView.as_view(),
        name="post-comments")
]
