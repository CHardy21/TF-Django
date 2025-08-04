from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'edited_at', 'content')
    search_fields = ('content', 'user__username', 'post__title')
    list_filter = ('created_at', 'post')
    readonly_fields = ('created_at', 'edited_at')
    
    def save_model(self, request, obj, form, change):
        obj.full_clean()  # Aplica las validaciones personalizadas
        super().save_model(request, obj, form, change)

