# apps/dashboard/middleware.py

from django.http import Http404
from django.urls import resolve

from apps import user


class SoloColaboradoresMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            ruta_actual = resolve(request.path_info).app_name
        except Exception:
            ruta_actual = None

        if ruta_actual == "dashboard":
            # if not request.user.is_authenticated or getattr(request.user, 'role', '') != 'colaborador':
            #     raise Http404("Página no encontrada")
            rol = getattr(user, "role", "")
            if rol not in ["colaborador", "administrador"] and not (
                user.is_staff or user.is_superuser
            ):
                raise Http404("Página no encontrada")
        return self.get_response(request)
