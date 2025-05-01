# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import RegisterView  # Import your RegisterView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
