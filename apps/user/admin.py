# # user/admin.py
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
# from .models import User  # tu modelo personalizado

# class CustomUserAdmin(UserAdmin):
#     model = User
#     # Campos que se muestran en el listado de usuarios
#     list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
#     list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'groups')
#     # Campos editables directamente
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Datos personales', {'fields': ('first_name', 'last_name', 'role')}),
#         ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
#     )
#     # Campos para crear un nuevo usuario desde el admin
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_superuser'),
#         }),
#     )

#     search_fields = ('username', 'email')
#     ordering = ('username',)

# # Registrar el modelo en el admin
# admin.site.register(User, CustomUserAdmin)


from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User

# 🔁 Reconfigurar el nombre del modelo Group
admin.site.unregister(Group)
Group._meta.verbose_name_plural = "Grupos"
admin.site.register(Group)

# 🛠️ Personalizar el panel de administración para User
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información personal'), {'fields': ('first_name', 'last_name', 'email', 'role')}),
        (_('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

