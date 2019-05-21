from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from plaid_django.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUser(generics.CreateAPIView):
    model = User
    permission_classes = [ AllowAny ]
    serializer_class = UserSerializer