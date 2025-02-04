# SPDX-License-Identifier: Apache-2.0 #

"""
Django settings for satool project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "8fHajN3#@7s(%-j8ny34GFHn23w&hb7d41lv-&*o@a-*nv8mx+^56n!!cj$!"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "modeltranslation",
    "corsheaders",
    "ckeditor",
    "django_ckeditor_5",
    "axes",
    "satool",
    "accounts",
    "questionnaires",
    "siteconfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    "axes.middleware.AxesMiddleware",
]

ROOT_URLCONF = "satool.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "../templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "satool.wsgi.application"

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the list
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Users
AUTH_USER_MODEL = "accounts.User"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_ADAPTER = "accounts.adapters.CustomAccountAdapter"
LOGIN_REDIRECT_URL = "/"


# Translation
MODELTRANSLATION_DEFAULT_LANGUAGE = "en"
MODELTRANSLATION_LANGUAGES = ("en", "es")
MODELTRANSLATION_AUTO_POPULATE = "default"
MODELTRANSLATION_CUSTOM_FIELDS = ("CKEditor5Field",)


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# API
API_VERSION = "1.0"

# Email
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "info@ovon.com")


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 12,
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
    "JWT_AUTH_COOKIE": "jwt-auth",
    "JWT_AUTH_REFRESH_COOKIE": "jwt-auth-refresh",
    "REGISTER_SERIALIZER": "accounts.serializers.CustomRegisterSerializer",
    "PASSWORD_RESET_USE_SITES_DOMAIN": True,
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=60),
}
# ALLAUTH CONFIG EMAILS TO HTML
ACCOUNT_EMAIL_TEMPLATE_EXTENSION = "html"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AXES CONFIG - Login attempts
AXES_LOCK_OUT_AT_FAILURE = True
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = timedelta(minutes=15)
AXES_RESET_ON_SUCCESS = True
AXES_ENABLE_ADMIN = True
AXES_LOCKOUT_PARAMETERS = ["ip_address", ["username", "user_agent"]]

BLEACH_STRIP_TAGS = True
BLEACH_STRIP_COMMENTS = True

FRONTEND_SERVER_URL = os.environ.get("FRONTEND_SERVER_URL", "")


# CK EDITOR
CKEDITOR_5_CONFIGS = {
    "basic": {
        "toolbar": ["heading", "bold", "italic", "underline", "|", "link"],
        "height": 400,
        "width": 600,
        "toolbarCanCollapse": False,
        "forcePasteAsPlainText": True,
        "autoParagraph": False,
    },
    "minimal": {
        "toolbar": ["link"],
        "height": 100,
        "width": 300,
        "toolbarCanCollapse": False,
        "forcePasteAsPlainText": True,
        "autoParagraph": False,
    },
}

SITE_ID = 1
