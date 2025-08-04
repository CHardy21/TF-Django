from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment
from apps.posts.models import Post

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, post=post, content=content)
        return redirect('post_detail', post_id=post.id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Permitir borrar si:
    # (1) el usuario creó el comentario
    # (2) el usuario es staff, superuser o pertenece al grupo 'admin'
    if (
        comment.user == request.user
        or request.user.is_staff
        or request.user.is_superuser
        or request.user.groups.filter(name='admin').exists()
    ):
        comment.delete()

    return redirect('post_detail', post_id=comment.post.id)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Verificamos si el usuario tiene permiso para editar
    if comment.user != request.user and not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("No tenés permiso para editar este comentario.")

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            comment.content = content
            comment.save()
            return redirect('show_post', post_id=comment.post.id)

    return render(request, 'comments/edit_comment.html', {'comment': comment})
