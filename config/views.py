from django.http import HttpResponse
from django.shortcuts import render
from apps.posts.models import Post
from django.http import JsonResponse

POSTS_POR_PAGINA = 4

def home(request):
    posts_recientes = Post.objects.filter(activo=True).order_by('-publicado')[:5]
    posts_destacados = Post.objects.filter(activo=True).order_by('-vistas')[:2]
    mas_leidos = Post.objects.filter(activo=True).order_by('-vistas')[:8]
    todos_los_posts = Post.objects.filter(activo=True).order_by('-publicado')
    primeros_posts = todos_los_posts[:POSTS_POR_PAGINA]

    return render(request, 'home.html', {
        'posts_recientes': posts_recientes,
        'posts_destacados': posts_destacados,
        'posts_mas_leidos': mas_leidos,
        'primeros_posts': primeros_posts,
    })


def index(request):
    return render(request, "index.html", {'user': request.user})

    
def Saludar(request):
    return HttpResponse("Hola Humano, estas en view Saludar!!!")

