from rest_framework.views import APIView
from .models import *
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from django.conf import settings


class ContentConfigView(APIView):
    def get(self, request, content_id):
        content = None
        legal_config = LegalSiteConfig.objects.filter(site__id=settings.SITE_ID).first()
        content_config = ContentSiteConfig.objects.filter(
            site__id=settings.SITE_ID
        ).first()
        if content_id == "terms":
            content = legal_config.terms_of_use
        elif content_id == "privacy":
            content = legal_config.privacy
        elif content_id == "cookies":
            content = legal_config.cookies
        elif content_id == "home":
            content = content_config.home
        elif content_id == "info":
            content = content_config.info
        else:
            raise ParseError("Invalid api param")
        return Response({"result": content})
