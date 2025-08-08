from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

# app_name = "posts"

urlpatterns = [
    path("", views.showAllPosts, name="posts"),
    path("load_posts/", views.load_posts, name="load_posts"),
    path("<int:post_id>/", views.showPost, name="show_post"),
    path("search/", views.search_posts, name="search_post"),
    path("new/", views.CreatePostView.as_view(), name="create_post"),
    path("categoria/<int:id>/", views.show_categoria, name="show_categoria"),
    path(
        "<int:pk>/edit/", login_required(views.EditPostView.as_view()), name="edit_post"
    ),
    path("<int:pk>/delete/", views.DeletePostView.as_view(), name="delete_post"),
]
