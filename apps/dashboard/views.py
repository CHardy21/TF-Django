# apps/dashboard/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.utils.dateparse import parse_date
from django.utils import timezone
from datetime import timedelta
from apps.posts.models import Post
from apps.comments.models import Comment
import csv


@login_required
def dashboard_colaborador(request):

    fecha_inicio_str = request.GET.get("fecha_inicio")
    fecha_fin_str = request.GET.get("fecha_fin")

    fecha_inicio = (
        parse_date(fecha_inicio_str) if isinstance(fecha_inicio_str, str) else None
    )
    fecha_fin = parse_date(fecha_fin_str) if isinstance(fecha_fin_str, str) else None

    if not fecha_inicio:
        fecha_inicio = timezone.now().date().replace(day=1)
    if not fecha_fin:
        fecha_fin = timezone.now().date()

    if fecha_inicio > fecha_fin:
        fecha_inicio, fecha_fin = fecha_fin, fecha_inicio

    posts = Post.objects.filter(
        autor=request.user, fecha__date__range=(fecha_inicio, fecha_fin)
    )

    total_posts = posts.count()
    publicados = posts.filter(publicado__lte=timezone.now().date()).count()
    borradores = total_posts - publicados
    total_comentarios = Comment.objects.filter(post__in=posts).count()
    promedio_vistas = posts.aggregate(Avg("vistas"))["vistas__avg"] or 0
    top_posts = posts.order_by("-vistas")[:5]

    context = {
        "posts": posts,
        "total_posts": total_posts,
        "publicados": publicados,
        "borradores": borradores,
        "total_comentarios": total_comentarios,
        "promedio_vistas": promedio_vistas,
        "top_posts": top_posts,
        "labels": [post.titulo for post in top_posts],
        "views": [post.vistas for post in top_posts],
        "fecha_inicio": fecha_inicio_str,
        "fecha_fin": fecha_fin_str,
    }
    return render(request, "dashboard_publicaciones.html", context)


@login_required
def exportar_estadisticas_csv(request):

    posts = Post.objects.filter(autor=request.user).order_by("-fecha_creacion")

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="estadisticas_colaborador.csv"'
    )

    writer = csv.writer(response)
    writer.writerow(["Título", "Fecha", "Vistas", "Comentarios", "Estado"])

    for post in posts:
        comentarios = Comment.objects.filter(post=post).count()
        estado = "Publicado" if post.publicado else "Borrador"
        writer.writerow(
            [post.titulo, post.fecha_creacion, post.vistas, comentarios, estado]
        )

    return response


@login_required
def publicaciones_view(request):

    posts = Post.objects.filter(autor=request.user)
    return render(request, "dashboard_publicaciones.html", {"posts": posts})


@login_required
def estadisticas_view(request):

    # Parámetros de rango de fecha
    fecha_inicio_str = request.GET.get("fecha_inicio")
    fecha_fin_str = request.GET.get("fecha_fin")
    rango = request.GET.get("rango")  # 'mes', '30d', 'historial'

    fecha_inicio = (
        parse_date(fecha_inicio_str) if isinstance(fecha_inicio_str, str) else None
    )
    fecha_fin = parse_date(fecha_fin_str) if isinstance(fecha_fin_str, str) else None

    hoy = timezone.now().date()

    # lógica según el rango
    if rango == "mes":
        fecha_inicio = hoy.replace(day=1)
        fecha_fin = hoy
    elif rango == "30d":
        fecha_inicio = hoy - timedelta(days=30)
        fecha_fin = hoy
    elif fecha_inicio and fecha_fin:
        if fecha_inicio > fecha_fin:
            fecha_inicio, fecha_fin = fecha_fin, fecha_inicio
    else:
        fecha_inicio = None
        fecha_fin = None

    posts = Post.objects.filter(autor=request.user)

    if fecha_inicio and fecha_fin:
        posts = posts.filter(fecha__date__range=(fecha_inicio, fecha_fin))

    total_posts = posts.count()
    publicados = posts.filter(publicado__lte=hoy).count()
    borradores = total_posts - publicados
    total_comentarios = Comment.objects.filter(post__in=posts).count()
    promedio_vistas = posts.aggregate(Avg("vistas"))["vistas__avg"] or 0
    top_posts = posts.order_by("-vistas")[:5]

    context = {
        "posts": posts,
        "total_posts": total_posts,
        "publicados": publicados,
        "borradores": borradores,
        "total_comentarios": total_comentarios,
        "promedio_vistas": round(promedio_vistas, 1),
        "top_posts": top_posts,
        "labels": [post.titulo for post in top_posts],
        "views": [post.vistas for post in top_posts],
        "fecha_inicio": fecha_inicio_str if fecha_inicio_str else "",
        "fecha_fin": fecha_fin_str if fecha_fin_str else "",
        "rango": rango or "",
    }

    return render(request, "dashboard_estadisticas.html", context)


@login_required
def top_view(request):

    posts = Post.objects.filter(autor=request.user).order_by("-vistas")[:10]

    return render(request, "dashboard_top.html", {"top_posts": posts})
