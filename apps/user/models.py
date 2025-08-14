# apps/user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('colaborador', 'Colaborador'),
        ('registrado', 'Registrado'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='registrado')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def is_admin(self):
        return self.role == 'admin'

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('images/default_avatar.png')  # Ruta relativa a static/

    class Meta:
        verbose_name_plural = "Usuarios"


