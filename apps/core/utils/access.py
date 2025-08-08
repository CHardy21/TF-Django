def has_dashboard_access(user):
    if not user.is_authenticated:
        return False
    rol = getattr(user, "role", "")
    return rol in ["colaborador", "administrador"] or user.is_staff or user.is_superuser
