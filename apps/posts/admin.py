# apps/posts/admin.py
from django.contrib import admin
from .models import Categoria, Post
from .forms import PostAdminForm
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostsAdmin(SummernoteModelAdmin):
    form = PostAdminForm
    list_display = (
        "id",
        "titulo",
        "fecha",
        "activo",
        "categoria",
        "publicado",
        "autor_display",
    )
    summernote_fields = ("resumen", "contenido")

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "imagen":
            if "request" in kwargs and kwargs["request"].resolver_match.kwargs.get(
                "object_id"
            ):
                post_id = kwargs["request"].resolver_match.kwargs["object_id"]
                try:
                    post = Post.objects.get(pk=post_id)
                    if post.imagen:
                        formfield.widget.attrs["data-initial"] = post.imagen.url
                except Post.DoesNotExist:
                    pass
        return formfield

    class Media:
        js = ("js/preview_imagen.js",)

    def autor_display(self, obj):
        return obj.autor.username if obj.autor else "anónimo"

    autor_display.short_description = "Autor"

    def save_model(self, request, obj, form, change):
        if not obj.autor:
            obj.autor = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields["autor"].disabled = True

        # Agregar data-initial con la URL de la imagen actual
        if obj and obj.imagen:
            form.base_fields["imagen"].widget.attrs["data-initial"] = obj.imagen.url

        return form


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")


admin.site.register(Categoria, CategoriaAdmin)
