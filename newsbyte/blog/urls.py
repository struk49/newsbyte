from django.urls import path, include
from blog.views import IndexView, DetailArticleView, CategoryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('article/<int:pk>/', DetailArticleView.as_view(), name='article-detail'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
