from django.db import models

# Create your models here.
class PostLiveManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        qureyset = queryset.filter(is_enabled=True)
        return queryset


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    is_enabled = models.BooleanField(default=False)
    publish_date = models.DateField(null=True, blank=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    live = PostLiveManager()
    
    def __str__(self):
        return f"{self.id}.{self.title}"


    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)