from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, Category
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ArticleForm


class IndexView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    # Removed paginate_by to display all blog posts in a single page
    ordering = ['-date']
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class DetailArticleView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'blog/blog_post.html'
    context_object_name = 'article'
    login_url = 'login'

class CategoryView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    login_url = 'login'

    def get_queryset(self):
        return Article.objects.filter(category__id=self.kwargs['category_id']).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('index')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


