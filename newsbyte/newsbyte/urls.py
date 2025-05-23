# project-level urls.py
from django.contrib import admin
from django.urls import path, include  # Include allows you to include app-specific urls
from users.views import RegisterView  # Import RegisterView for homepage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # blog-related URLs
    path('users/', include('users.urls')),  # users-related URLs
    path('', RegisterView.as_view(), name='register'),  # Homepage is now RegisterView
    path('shop/', include('shop.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  

