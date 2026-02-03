from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "posts"
    )    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"post by {self.author.username}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name=  "post_comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"comment by {self.author.username}"
    
