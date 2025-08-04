# apps/user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

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
    
    class Meta:
        verbose_name_plural = "Usuarios"
