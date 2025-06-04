# project-level urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import RegisterView  # Homepage view (register)

urlpatterns = [
    path('admin/', admin.site.urls),

    # App URL includes
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('shop/', include('shop.urls')),

    # Pages app URLs
    path('', include('pages.urls')),

    # Homepage: registration view
    path('', RegisterView.as_view(), name='register'),
]

# Serve media files in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
