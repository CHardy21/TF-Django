# apps/core/views.py
from django.shortcuts import render


def error_403_view(request, exception):
    return render(request, "no_autorizado.html", status=403)


def error_404_view(request, exception):
    return render(request, "no_encontrado.html", status=404)


def error_500_view(request):
    return render(request, "error_servidor.html", status=500)
