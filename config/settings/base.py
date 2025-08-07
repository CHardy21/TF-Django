
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
BASE_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    # Mis Apps
    'apps.core', # app para mantener utilidades comunes a todas la apps como filtros, y mas...
    'apps.posts',
    'apps.user',
    'apps.comments',
    'apps.dashboard',
    
]

THIRDS_APPS = [
    # Apps de terceros
    'django_summernote',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRDS_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Mis middleware...
    'apps.dashboard.middleware.SoloColaboradoresMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR),'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(os.path. dirname(BASE_DIR),'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SUMMERNOTE_CONFIG = {
    'iframe': True,  # Usar iframe (modo por defecto)
    'summernote': {
        
      
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'clear']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
        'lang': 'es-ES',  # Idioma del editor
    },
    'attachment_require_authentication': True,
    'disable_attachment': False,
}

SUMMERNOTE_THEME = 'bs5'
 
# Panel de Control
JAZZMIN_SETTINGS = {
    "site_title": "Panel de Info2025",
    "site_header": "Administración",
    "site_brand": "CHardy",
    "welcome_sign": "Bienvenido al Panel de Administración",
    "copyright": "CHardy Dev",
    "user_avatar": None,
 
    "topmenu_links": [
        {
            "name": "Ver sitio",
            "url": "/",  # Ruta principal del sitio
            "new_window": True,  # Abre en nueva pestaña
        },
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
    
    # "order_with_respect_to": [
    #     "user.User",
    #     "auth.Group",
    # ],
    
    "hide_apps": ["auth", "django_summernote","post", "categoria",],
   
    
    "custom_links": {
    "user": [
        {
            "name": "Grupos",
            "url": "admin:auth_group_changelist",
            "icon": "fas fa-users"
        }
    ],
    "post": [  
            {
                "name": "Comentarios",
                "url": "admin:comments_comments_changelist",
                "icon": "fas fa-comments"
            },
            {
                "name": "Posts",
                "url": "admin:post_post_changelist",
                "icon": "fas fa-newspaper"
            },
            {
                "name": "Categorías",
                "url": "admin:categoria_categoria_changelist",
                "icon": "fas fa-tags"
            }
        ]
    },

    
    "show_sidebar": True,
    "navigation_expanded": True,
}
