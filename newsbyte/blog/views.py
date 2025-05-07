from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article

class IndexView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 1
    ordering = ['-date']
    login_url = 'login'


class DetailArticleView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'blog/blog_post.html'
    context_object_name = 'article'
    login_url = 'login'


