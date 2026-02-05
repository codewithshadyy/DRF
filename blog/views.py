from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from  rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
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
        
class UserListView(ListAPIView):
    
    serializer_class= UserSerializer
    queryset = User.objects.all() 
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'email']  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']
    
    
class UserOrderListView(ListAPIView):
    serializer_class= UserSerializer
    queryset = User.objects.all() 
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email']          