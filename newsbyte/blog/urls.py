# blog/urls.py
from django.urls import path, include
from blog.views import IndexView  # Import IndexView from views.py

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Homepage URL points to IndexView
    path('tinymce/', include('tinymce.urls')),
    # Other blog-specific URLs, e.g.:
    # path('post/<int:id>/', PostDetailView.as_view(), name='post_detail'),
]
