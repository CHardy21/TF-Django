# apps/comments/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from apps.posts.models import Post

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"

    def clean(self):
        if len(self.content.strip()) < 3:
            raise ValidationError("El comentario debe tener al menos 3 caracteres.")
