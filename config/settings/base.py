from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Aplicaciones
BASE_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.core",
    "apps.posts",
    "apps.user",
    "apps.comments",
    "apps.dashboard",
]

THIRDS_APPS = [
    "django_summernote",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRDS_APPS

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middleware.access_control.SoloColaboradoresMiddleware",
    "apps.core.middleware.access_control.OcultarAdminMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Usuario personalizado
AUTH_USER_MODEL = "user.User"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Internacionalización
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True

# Archivos estáticos y media
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Clave primaria por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Configuración de Summernote
SUMMERNOTE_CONFIG = {
    "iframe": True,
    "summernote": {
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "italic", "underline", "clear"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["insert", ["link", "picture", "video"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ],
        "lang": "es-ES",
    },
    "attachment_require_authentication": True,
    "disable_attachment": False,
}
SUMMERNOTE_THEME = "bs5"

# Configuración de Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "Panel de Info2025",
    "site_header": "Administración",
    "site_brand": "CHardy",
    "welcome_sign": "Bienvenido al Panel de Administración",
    "copyright": "CHardy Dev",
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Ver sitio", "url": "/", "new_window": True},
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "user.User"},
        {"model": "auth.Group"},
    ],
    "icons": {
        "user.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "post.Post": "fas fa-newspaper",
        "categoria.Categoria": "fas fa-tags",
    },
    "hide_apps": ["auth", "django_summernote", "post", "categoria"],
    "custom_links": {
        "user": [{"name": "Grupos", "url": "admin:auth_group_changelist", "icon": "fas fa-users"}],
        "post": [
            {"name": "Comentarios", "url": "admin:comments_comments_changelist", "icon": "fas fa-comments"},
            {"name": "Posts", "url": "admin:post_post_changelist", "icon": "fas fa-newspaper"},
            {"name": "Categorías", "url": "admin:categoria_categoria_changelist", "icon": "fas fa-tags"},
        ],
    },
    "show_sidebar": True,
    "navigation_expanded": True,
}
