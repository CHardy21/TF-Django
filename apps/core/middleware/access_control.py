from apps.core.utils.access import has_dashboard_access
from django.urls import resolve
from django.shortcuts import render
from django.http import HttpResponseNotFound


class SoloColaboradoresMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            ruta_actual = resolve(request.path_info).app_name
        except Exception:
            ruta_actual = None

        if ruta_actual == "dashboard" and not has_dashboard_access(request.user):
            return HttpResponseNotFound(render(request, "no_encontrado.html"))

        return self.get_response(request)


class OcultarAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin/"):
            user = request.user
            if not user.is_authenticated or not (user.is_staff or user.is_superuser):
                return HttpResponseNotFound(render(request, "no_encontrado.html"))
        return self.get_response(request)
