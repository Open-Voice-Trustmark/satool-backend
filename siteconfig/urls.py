# SPDX-License-Identifier: Apache-2.0 #

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(
        r"^site/(?P<content_id>|cookies|terms|privacy|home|info)$",
        views.ContentConfigView.as_view(),
    ),
]
