from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article

class IndexView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    # Removed paginate_by to display all blog posts in a single page
    ordering = ['-date']
    login_url = 'login'

class DetailArticleView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'blog/blog_post.html'
    context_object_name = 'article'
    login_url = 'login'
