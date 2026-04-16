
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from store.views import fix_admin   

urlpatterns = [
    path('fix-admin-123/', fix_admin),
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    
]

# To display images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)