from main.settings.base import *

DEBUG = True

# ============================================================ [OTHER SETTINGS]
WSGI_APPLICATION = "main.sgi.wsgi_debug.application"

# ========================================================= [DATABASE SETTINGS]
DATABASES["default"]["HOST"] = "localhost"

# =================================== [MEDIA AND STATIC PATH - AWS S3 SETTINGS]
MEDIA_URL = "/media/"
STATIC_URL = "/static/"

# ======================================================== [TEMPLATES SETTINGS]
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG
TEMPLATES[0]["OPTIONS"]["loaders"] = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader"
]