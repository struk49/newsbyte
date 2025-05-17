# blog/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'featured', 'image']  # Include 'image' field

        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
