from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.urls import include
from .views import *

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', views.about_view, name='about'),
    path('', include('apps.posts.urls')),
    path("user/", include("apps.user.urls", namespace="user")),
    path('comments/', include('apps.comments.urls')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    
    # Complementos instalados
    path('summernote/', include('django_summernote.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

