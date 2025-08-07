# apps/posts/views.py
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from apps.posts.forms import PostForm
from apps.comments.models import Comment
from apps.posts.models import Post, Categoria

from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

def showAllPosts(request):
    all_posts = Post.objects.all().order_by('-fecha') 
    paginator = Paginator(all_posts, 8)  # Mostrar 8 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/posts_show_all.html', {
        'page_obj': page_obj
    })

def showPost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    related_post = Post.objects.filter(categoria=post.categoria).exclude(id=post.id)[:3]

    post.vistas += 1
    post.save(update_fields=['vistas'])

    can_edit_or_delete = (
        request.user == post.autor
        or request.user.is_staff
        or request.user.is_superuser
        or request.user.groups.filter(name='admin').exists()
    )

    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST.get('content', '').strip()
            if content:
                Comment.objects.create(post=post, user=request.user, content=content)
                return redirect('show_post', post_id=post.id)
        else:
            return redirect('login')

    return render(request, 'posts/posts_show.html', {
        'post': post,
        'comments': comments,
        'can_edit_or_delete': can_edit_or_delete,
        'relacionados': related_post,
    })

def show_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    posts_list = Post.objects.filter(categoria=categoria)

    paginator = Paginator(posts_list, 8)  # 6 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/categoria_show.html', {
        'categoria': categoria,
        'page_obj': page_obj
    })


def load_posts(request):
    offset = int(request.GET.get('offset', 0))
    POSTS_POR_PAGINA = 4

    nuevos_posts = Post.objects.filter(activo=True).order_by('-publicado')[offset:offset+POSTS_POR_PAGINA]

    html = render_to_string('partials/list_posts.html', {
        'todos_los_posts': nuevos_posts
    }, request=request)

    # Verificar si quedan más
    total_posts = Post.objects.filter(activo=True).count()
    quedan_posts = offset + POSTS_POR_PAGINA < total_posts

    return JsonResponse({
        'html': html,
        'quedan_posts': quedan_posts
    })



def search_posts(request):
    q = request.GET.get("q", "")
    fecha_inicio = request.GET.get("fecha_inicio")
    fecha_fin = request.GET.get("fecha_fin")
    categoria = request.GET.get("categoria")

    resultados = Post.objects.all()

    if q:
        resultados = resultados.filter(titulo__icontains=q) | resultados.filter(resumen__icontains=q)

    if fecha_inicio:
        resultados = resultados.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        resultados = resultados.filter(fecha__lte=fecha_fin)
    if categoria:
        resultados = resultados.filter(categoria_id=categoria)

    filtros_aplicados = q or fecha_inicio or fecha_fin or categoria

    paginator = Paginator(resultados, 6)  # 6 resultados por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "posts/posts_search.html", {
        "categorias": Categoria.objects.all(),
        "filtros_aplicados": filtros_aplicados,
        "resultados": page_obj,  
    })

# ------------------------
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  
            post.save()
            return redirect('show_post', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {
        'form': form
    })

class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_edit.html'  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        user = request.user
        if not (
            user == self.object.autor
            or user.is_staff
            or user.is_superuser
            or user.groups.filter(name='admin').exists()
        ):
            return redirect('show_post', pk=self.object.pk)

        return super().dispatch(request, *args, **kwargs)

    def reemplazar_imagen(self, post):
        imagen_nueva = self.request.FILES.get('imagen')
        if imagen_nueva:
            if post.imagen and post.imagen.name != 'posts/post_default.png':
                post.imagen.delete(save=False)
            post.imagen = imagen_nueva

    def form_valid(self, form):
        post = form.instance
        self.reemplazar_imagen(post)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return redirect('show_post', pk=self.object.pk).url
    def get_success_url(self):
        return reverse('show_post', kwargs={'post_id': self.object.pk})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if not (
        request.user == post.autor
        or request.user.is_staff
        or request.user.is_superuser
        or request.user.groups.filter(name='admin').exists()
    ):
        return HttpResponse("No tenés permiso para eliminar este post", status=403)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    return render(request, 'posts/post_confirm_delete.html', { 'post': post })

