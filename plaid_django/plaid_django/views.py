from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from plaid_django.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login
from rest_framework import status

User = get_user_model()

class CreateUser(generics.CreateAPIView):
    model = User
    permission_classes = [ AllowAny ]
    serializer_class = UserSerializer

@api_view(['POST'])
@permission_classes((AllowAny, ))
def Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        Token.objects.filter(user = user).delete()
        token = Token.objects.create(user = user)
        return Response({"token_type": "Token", "token" : token.key}, status=status.HTTP_201_CREATED)
    return Response({"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def Logout(request):
    Token.objects.filter(user = request.user).delete()
    return Response()