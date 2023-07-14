from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^me$", views.UserViewSet.as_view({"get": "retrieve", "post": "update"})),
]
