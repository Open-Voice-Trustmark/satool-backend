# SPDX-License-Identifier: Apache-2.0 #

from django.urls import path, re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"sections", views.SectionViewSet, basename="sections")
router.register(
    r"questionnaires", views.UserQuestionnaireViewSet, basename="questionnaires"
)

urlpatterns = [
    re_path(
        "^questions/(?P<questionnaire>[-\d]+)/(?P<section>[-\d]+)$",
        views.QuestionViewSet.as_view({"get": "list"}),
    ),
    re_path(
        "^questions/(?P<questionnaire>[-\d]+)/question/(?P<question>[-\d]+)$",
        views.QuestionViewSet.as_view({"get": "list"}),
    ),
    re_path(
        "^questionnaire/(?P<questionnaire>[-\d]+)$",
        views.QuestionnaireView.as_view(),
    ),
    re_path(
        "^questionnaire/new$",
        views.CreateQuestionnaireView.as_view(),
    ),
    re_path(
        "^questionnaire/(?P<questionnaire>[-\d]+)/answers$",
        views.AnswersView.as_view(),
    ),
    re_path(
        "^results/(?P<questionnaire>[-\d]+)$",
        views.ResultsView.as_view(),
    ),
    path("", include(router.urls)),
]
