from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(LegalSiteConfig)
class LegalSiteConfigTranslationOptions(TranslationOptions):
    fields = ("terms_of_use", "privacy", "cookies")


@register(ContentSiteConfig)
class ContentSiteConfigTranslationOptions(TranslationOptions):
    fields = ("home", "info")
