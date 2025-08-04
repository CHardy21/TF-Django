=======================================================     
      TRABAJO FINAL con Django (Informatorio 2025)
=======================================================

consignas:

1. Sistema de Autenticación y Perfiles
--------------------------------------
 * Diseñar modelo de usuarios con roles (admin, registrado).
 * Implementar registro de usuarios (formulario + validación).
 * Crear sistema de login/logout.
 * Middleware para restringir rutas (solo usuario creador puede eliminar/modificar posts/comentarios).

2. Gestión de Posts
-------------------
 * Modelo de Post (campos: título, contenido, fecha, categoría, autor, etc.).
 * Formulario para crear/editar posts (solo usuarios autenticados).
 * Lógica para eliminar/modificar posts:
      - Admin puede borrar cualquier post/cometario.
      - Usuario registrado solo puede borrar/modificar sus propios posts/comentarios.

3. Comentarios
--------------
- Modelo de Comentario (relacionado con Post y User).
- Formulario para comentar (solo usuarios registrados).
- Validar que el usuario esté autenticado para comentar.
- Opción para editar/eliminar comentarios (mismas restricciones que posts).

4. Filtros y Búsquedas
----------------------
* Filtrar posts por:
 - Fecha (rango o específica).
 - Categoría (dropdown o tags).
* Número de comentarios (ej: "más populares primero").

5. Extra
--------
* Paginación de resultados (evitar sobrecarga en listados).
* Notificaciones (ej: cuando alguien comenta tu post).
* Sistema de "likes" o votos a posts/comentarios.

. Deployment
------------
Despliegue en plataforma PythonAnyWhere