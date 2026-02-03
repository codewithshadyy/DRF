from .models import Post, Comment
from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "username"]

        
        
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    
    class Meta:
        model = Comment
        fields = ["id", "text", "author", "created_at"] 
        

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ["id", "content", "author", "comments", "created_at"]        
        
        
              
       
       