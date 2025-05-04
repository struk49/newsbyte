# blog/views.py
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article

class IndexView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'blog/index.html'

    def get(self, request):
        articles = Article.objects.all().order_by('-date')  # Fetch latest articles
        return render(request, self.template_name, {'articles': articles})
