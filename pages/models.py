from django.db import models
from django.urls import reverse, reverse_lazy
from taggit.managers import TaggableManager

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    def __str__(self):
        return self.title

        
