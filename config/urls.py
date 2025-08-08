from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import home, about_view

# Handlers de errores definidos como variables globales
handler403 = "apps.core.views.error_403_view"
handler404 = "apps.core.views.error_404_view"
handler500 = "apps.core.views.error_500_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about_view, name="about"),
    path("posts/", include("apps.posts.urls")),
    path("user/", include("apps.user.urls", namespace="user")),
    path("comments/", include("apps.comments.urls")),
    path("dashboard/", include("apps.dashboard.urls", namespace="dashboard")),
    path("summernote/", include("django_summernote.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
