from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from  rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class  PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
        
class CommentListCreateAPIView(ListCreateAPIView):
    
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        return Comment.objects.filter(post_id=post_id)
    
    
    def perform_create(self, serializer):
        serializer.save(
            author = self.request.user,
            post_id = self.kwargs["post_id"]            
                        )        