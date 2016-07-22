# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%l-z12#+$xtw-syvyq&gwa=_sqyxc7-r1n_fzh+kg_7nsh^vv0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # START django manage.py built apps
    'students',
    # END django manage.py built apps
    # START third-party packages app
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_docs', # Documentation of Django Rest Framework
    'corsheaders',
    'django_logging',
    'markdown',
    # END third-party packages app
    
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django_logging.middleware.DjangoLoggingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'student_list_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media', # To Add Media URLS on templates
            ],
        },
    },
]

WSGI_APPLICATION = 'student_list_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# UNCOMMENT STATIC ROOT to run collectstatic
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# COMMENT STATIC_PATH to run collecstatic
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# COMMENT STATICFIELS_DIRS to run collecstatic
STATICFILES_DIRS = (STATIC_PATH, )

# START Django Rest Framework settings
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    # ),
    # Disables the Admin UI of the Django Rest Framework
    # Source: http://stackoverflow.com/questions/11898065/how-to-disable-admin-style-browsable-interface-of-django-rest-framework
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # )
}
# END Django Rest Framework settings

CORS_ORIGIN_ALLOW_ALL = True

# START Logging
DJANGO_LOGGING = {
    "INFO":
    {
        "timestamp":
        {
            "request": {
            # ... request info ...
            },
            "response": {
            # ... response info ...
            }
        }
    },
    "SQL_LOG" : False,
}
# END Logging