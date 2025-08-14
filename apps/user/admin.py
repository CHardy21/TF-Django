from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import User
from django import forms
from apps.core.widgets import AdminAvatarWidget  # Ajustá el import según tu estructura

# Reconfigurar el nombre del modelo Group
admin.site.unregister(Group)
Group._meta.verbose_name_plural = "Grupos"
admin.site.register(Group)

# Personalizar el panel de administración para User

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'avatar': AdminAvatarWidget,
        }

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    form = UserAdminForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información personal'), {'fields': ('avatar', 'first_name', 'last_name', 'email', 'role')}),
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
    
    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="height:40px; border-radius:50%;" />', obj.avatar.url)
        return "Sin avatar"

