# blog/views.py
from django.shortcuts import render
from django.views import View  # This is the key import
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, View):  # Now it should recognize View
    login_url = 'login'  # optional, defines the login URL if not set in settings.py

    def get(self, request):
        return render(request, 'blog/index.html')  # Render your template
