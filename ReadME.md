# -----------------------------------
#  Trabajo Final - Informatorio 2025
# -----------------------------------

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

El sistema define **tres perfiles de usuario** con diferentes niveles de acceso:

### ⚫ Visitante (no registrado)
- Navegar libremente por la web.
- Filtrar publicaciones por categoría, fecha y orden alfabético.
- Leer artículos.
- Registrarse e iniciar sesión.

### 🟢 Miembro (Usuario Registrado)
Incluye los permisos de un visitante, más:
- Comentar en artículos.
- Editar y eliminar sus propios comentarios.
- Cerrar sesión.

### 🟣 Administrador
Incluye todos los permisos anteriores, más:
- Crear, editar y eliminar artículos.
- Subir, editar y eliminar imágenes asociadas.
- Categorizar artículos.
- Editar o eliminar comentarios de otros usuarios.


---

## 🧱 Estructura del Sitio

- **Inicio / Portada**  
  Muestra publicaciones recientes o destacadas.

- **Categorías**  
  Organización temática del contenido del blog.

- **Acerca de**  
  Presentación del blog, sus autores y propósito.

- **Contacto**  
  Información de contacto, incluyendo:
  - Formulario (opcional).
  - Dirección de correo.
  - Enlaces a redes sociales.


---

## 🔧 Funcionalidades Implementadas

### 📄 Artículos
- Crear
- Leer
- Editar
- Eliminar

### 💬 Comentarios
- Crear
- Leer
- Editar
- Eliminar

### 🔍 Filtros de búsqueda
- Por categoría
- Por antigüedad (ascendente/descendente)
- Por orden alfabético (A-Z / Z-A)

### 👤 Gestión de usuarios
- Registro de nuevos usuarios
- Login / Logout
- Asignación de roles por permisos


---

## ⚙️ Instalación y ejecución local

### 1. Clona el repositorio

```
git clone git@github.com:v-hardy/blog-django.git
cd blog-django
```

### 2. Crea y activa un entorno virtual

```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala dependencias

```
pip install -r requirements.txt
```

### 4. Aplica migraciones

```
python manage.py migrate
```

### 5. Ejecuta el servidor de desarrollo

```
python manage.py runserver
```
Accede en tu navegador a: http://localhost:8000


---

## 🤝 Contribuciones

¡Contribuciones son bienvenidas!
Puedes abrir un issue para reportar bugs o sugerencias, o enviar un pull request para proponer mejoras.


---

## ✉️ Contacto

Si deseas saber más o ponerte en contacto con el equipo detrás del proyecto, escribe a: victor.hardy@hotmail.com


---