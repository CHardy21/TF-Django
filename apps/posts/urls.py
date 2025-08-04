# apps/post/urls.py
from django.urls import path
from .views import *
from .views import EditPostView

from . import views

urlpatterns = [
    path('posts/', showAllPosts, name='posts'),
    path('posts/load_posts/', views.load_posts, name='load_posts'),
    path('posts/<int:post_id>/', showPost, name='show_post'),
    path('posts/search/', search_posts, name='search_post'),
    path('posts/new/', views.create_post, name='create_post'),
    path('posts/categoria/<int:id>/', views.show_categoria, name='show_categoria'),

    # URLs para editar/eliminar posts
    path('posts/<int:pk>/edit/', login_required(EditPostView.as_view()), name='edit_post'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]

