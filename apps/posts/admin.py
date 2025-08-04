from django.contrib import admin
from .models import Categoria, Post
from .forms import PostAdminForm
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostsAdmin(SummernoteModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'titulo', 'fecha', 'activo', 'categoria', 'publicado', 'autor_display')
    # list_select_related = ('categoria', )  # Para evitar consultas duplicadas

    # def categoria_descripcion(self, obj):
    #     return obj.categoria.descripcion
    # categoria_descripcion.short_description = 'Descripción categoría'
    
    def autor_display(self, obj):
        return obj.autor.username if obj.autor else "anónimo"
    autor_display.short_description = 'Autor'

    def save_model(self, request, obj, form, change):
        if not obj.autor:
            obj.autor = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['autor'].disabled = True
        return form

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    
admin.site.register(Categoria, CategoriaAdmin)
