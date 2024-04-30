# SPDX-License-Identifier: Apache-2.0 #

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.sites.models import Site
from django.conf import settings


class ContentSiteConfig(models.Model):
	site = models.OneToOneField(Site, on_delete=models.CASCADE, blank=False)
	home = CKEditor5Field(blank=True, config_name="basic")
	info = CKEditor5Field(blank=True, config_name="basic")

	def __str__(self):
		return "Content config for site " + str(self.site)


class LegalSiteConfig(models.Model):
	site = models.OneToOneField(Site, on_delete=models.CASCADE, blank=False)
	terms_of_use = CKEditor5Field(blank=True, config_name="basic")
	privacy = CKEditor5Field(blank=True, config_name="basic")
	cookies = CKEditor5Field(blank=True, config_name="basic")

	def __str__(self):
		return "Legal config for site " + str(self.site)
