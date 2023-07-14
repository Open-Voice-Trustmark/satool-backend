from django.contrib import admin
from .models import *


@admin.register(LegalSiteConfig)
class LegalSiteConfigAdmin(admin.ModelAdmin):
    list_display = ("site",)
    readonly_fields = [
        "id",
    ]
    fields = (
        "site",
        "terms_of_use_en",
        "terms_of_use_es",
        "privacy_en",
        "privacy_es",
        "cookies_en",
        "cookies_es",
    )
    search_fields = [
        "site",
    ]
    ordering = ("-site",)


@admin.register(ContentSiteConfig)
class ContentSiteConfigAdmin(admin.ModelAdmin):
    list_display = ("site",)
    readonly_fields = [
        "id",
    ]
    fields = (
        "site",
        "home_en",
        "home_es",
        "info_en",
        "info_es",
    )
    search_fields = [
        "site",
    ]
    ordering = ("-site",)
