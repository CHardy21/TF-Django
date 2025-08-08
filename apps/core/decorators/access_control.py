from functools import wraps
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from apps.core.utils.access import has_dashboard_access


# def require_dashboard_access(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if not has_dashboard_access(request.user):
#             raise Http404("Página no encontrada")
#         return view_func(request, *args, **kwargs)

#     return _wrapped_view


def require_dashboard_access(raise_404=True):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not has_dashboard_access(request.user):
                if raise_404:
                    raise Http404("Página no encontrada")
                return redirect(settings.HANDLER404)  # o una vista personalizada
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
