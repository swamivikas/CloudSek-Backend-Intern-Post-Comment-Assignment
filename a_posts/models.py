from django.db import models
import uuid
from django.contrib.auth.models import User

class Post(models.Model):
    title =models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    url = models.URLField(max_length=500,null=True)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4,unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering =['-created']
    


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}' 
        except:
            return f'no author : {self.body[:30]}' 
        
    class Meta:
        ordering = ['-created']
