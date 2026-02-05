
from .views import PostListCreateAPIView, CommentListCreateAPIView, UserListView, UserOrderListView
from django.urls import path

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="posts" ),
    path(  "posts/<int:post_id>/comments/",
        CommentListCreateAPIView.as_view(),
        name="post-comments"),
    path("users", UserListView.as_view(), name="users"),
    # path("users", UserOrderListView.as_view(), name="ordering")
]
