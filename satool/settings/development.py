from satool.settings.common import *

DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "localhost:3000",
    "http://localhost:3000",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
    }
}

MIDDLEWARE_DEBUG = ["satool.middleware.TimeDelayMiddleware"]
MIDDLEWARE.extend(MIDDLEWARE_DEBUG)

DEBUG_REQUEST_TIME_DELAY = 0.2

EMAIL_USE_TLS = False
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CORS_ORIGIN_ALLOW_ALL = True
