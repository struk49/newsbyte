from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = HTMLField()  # Store raw HTML content
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)  # ✅ Add this line

    def __str__(self):
        return self.title
