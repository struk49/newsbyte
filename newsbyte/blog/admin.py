from django.contrib import admin
from .models import Article, Category
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
    list_display = ('title', 'author', 'date', 'category')  # Optional: shows category in list


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

