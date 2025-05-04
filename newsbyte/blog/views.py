from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article

class IndexView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 1
    ordering = ['-date']
    login_url = 'login'
