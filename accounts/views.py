# SPDX-License-Identifier: Apache-2.0 #

from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User
import random
import string


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def update(self, request):
        user = request.user
        user.first_name = request.data.get("first_name", "")
        user.last_name = request.data.get("last_name", "")
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def retrieve(self, request):
        return Response(UserSerializer(request.user).data)
