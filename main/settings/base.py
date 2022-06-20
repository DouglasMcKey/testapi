from pathlib import Path

# ============================================================= [PATH SETTINGS]
BASE_DIRECTORY = Path(__file__).resolve(strict=True).parent.parent.parent
MEDIA_DIRECTORY = BASE_DIRECTORY / "media"
STATIC_DIRECTORY = BASE_DIRECTORY / "static"
STATICFILES_DIRS = [STATIC_DIRECTORY]

# ================================================ [STANDARD SECURITY SETTINGS]
SECRET_KEY = "CustomDjangoSecretKey---------------------------------------------"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 28800
CSRF_USE_SESSIONS = True
X_FRAME_OPTIONS = "DENY"

ADMINS = [("System Administrator", "support@testapi.com")]
MANAGERS = ADMINS

INTERNAL_IPS = ["127.0.0.1"]
ALLOWED_HOSTS = [
    "127.0.0.1", "localhost", "http://localhost:8000"
]

# ========================================================= [DATABASE SETTINGS]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "PORT": 3306,
        "NAME": "testapi",
        "USER": "testapi",
        "PASSWORD": "testapi",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# ============================================= [INTERNATIONALIZATION SETTINGS]
TIME_ZONE = "Africa/Johannesburg"
LANGUAGE_CODE = "en-us"
USE_I18N = False
USE_TZ = True

# ============================================ [INSTALLED APPLICATION SETTINGS]
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_countries",
    "django_extensions",
    "django_filters",
    "widget_tweaks",
    "storages",
    "rest_framework",
    "api.apps.APIConfig",
    "main.apps.MainConfig",
    "transactions.apps.TransactionsConfig"
]

# ======================================================== [TEMPLATES SETTINGS]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIRECTORY],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages"
            ]
        }
    }
]

# ======================================================= [MIDDLEWARE SETTINGS]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.http.ConditionalGetMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware"
]

# =================================================== [REST FRAMEWORK SETTINGS]
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100
}

# ============================================================ [OTHER SETTINGS]
SITE_TITLE = "Test API"
SITE_VERSION = "1.0"
SITE_DOMAIN = "www.testapi.com"
SITE_AUTHOR = f"{SITE_TITLE} - {SITE_DOMAIN}"
SITE_DESCRIPTION = f"{SITE_TITLE} - All rights reserved. {SITE_TITLE} |" \
                   f" Site Version: {SITE_VERSION}"

ROOT_URLCONF = "main.urls"
