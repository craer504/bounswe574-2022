from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('space.urls')),
    path('quiz/', include('quiz.urls')),
    path('',include('annotator.urls')),
    path('',include('annotation.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
