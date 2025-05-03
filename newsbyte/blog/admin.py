from django.contrib import admin
from .models import Article

# Register your models here.
class Article(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'featured')
    kist_display_links = ('title', 'author')
    serch_feilds = ('title', 'author', 'content')
    list_display_links = ('title', 'autor')
    list_filter = ('author' 'date', 'featured')
    

    #Register your models here
    admin.site.register(Article)




