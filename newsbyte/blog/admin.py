from django.contrib import admin
from .models import Article
from tinymce.widgets import TinyMCE
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': TinyMCE(),
        }

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)
