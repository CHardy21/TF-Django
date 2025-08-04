
#  Trabajo Final - Informatorio 2025


# 📰 Blog Platform - Sistema de Gestión de Contenido

Este proyecto es una plataforma web tipo **blog**, desarrollada con el framework **Django**. Su objetivo es ofrecer una solución completa y escalable para la publicación, gestión y exploración de artículos, incorporando distintos niveles de permisos mediante roles de usuario (Administrador, Colaborador, Registrado).

---

## 🧑‍💻 Tecnologías Utilizadas

- **Django** (backend y lógica de negocio)
- **HTML5** (estructura del frontend)
- **Bootstrap** (Script, CSS, Icons)
- **JS** (JS, Ajax)
- **SQLite3** (base de datos por defecto en Django)


---

## 🎯 Características Principales

El sistema define **cuatro perfiles de usuario** con diferentes niveles de acceso:

### ⚫ Visitante (no registrado)
- Navegar libremente por la web.
- Filtrar publicaciones por categoría, fecha y orden alfabético.
- Leer artículos.
- Registrarse e iniciar sesión.

### 🟢 Registrado (Usuario con Rol 'registrado')
Incluye los permisos de un visitante, más:
- Comentar en artículos.
- Editar y eliminar sus propios comentarios.
- Cerrar sesión.

### 🟢 Colaborador (Usuario con Rol 'colaborador')
Incluye los permisos de un registrado, más:
- Publicar artículos (post).
- Editar y eliminar sus propios post y comentarios.
- Cerrar sesión.

### 🟣 Administrador (rol 'administrador')
Incluye todos los permisos anteriores, más:
- Crear, editar y eliminar artículos.
- Subir, editar y eliminar imágenes asociadas.
- Categorizar artículos.
- Editar o eliminar comentarios de otros usuarios.


## 🤝 Contribuciones

¡Contribuciones son bienvenidas!

---
