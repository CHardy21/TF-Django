# apps/post/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
from django_summernote.fields import SummernoteTextField


class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=150, null=False)
    imagen = models.ImageField(
        null=True, blank=True, upload_to="posts", default="posts/post_default.png"
    )
    resumen = SummernoteTextField(max_length=1000, null=False, blank=True)
    contenido = SummernoteTextField(
        null=False, verbose_name="Escriba aquí el contenido"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True
    )
    publicado = models.DateField(default=timezone.now)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    vistas = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-publicado",)

    def __str__(self) -> str:
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        # if self.imagen and self.imagen.name != 'posts/post_default.png':
        #    self.imagen.delete(save=False)
        super().delete(using=using, keep_parents=keep_parents)

    def user_can_edit(self, user):
        return self.autor == user
