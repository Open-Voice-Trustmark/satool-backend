# SPDX-License-Identifier: Apache-2.0 #

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.sites.models import Site
from django.conf import settings


class ContentSiteConfig(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, blank=False)
    home = RichTextField(blank=True, config_name="basic")
    info = RichTextField(blank=True, config_name="basic")

    def __str__(self):
        return "Content config for site " + str(self.site)


class LegalSiteConfig(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, blank=False)
    terms_of_use = RichTextField(blank=True, config_name="basic")
    privacy = RichTextField(blank=True, config_name="basic")
    cookies = RichTextField(blank=True, config_name="basic")

    def __str__(self):
        return "Legal config for site " + str(self.site)
