from Item.models import AccessToken
from Item.models import AccessToken
from Item.serializers import AccessTokenSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes

class AccessTokenCreate(generics.CreateAPIView):
    # """
    #     POST:
    #     Create an accessToken from the public key.
    # """

    serializer_class = AccessTokenSerializer
    
    def get_queryset(self):
        user  = self.request.user
        return AccessToken.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def handleWebhook(request):
    if request.method == 'POST':
        print(request.data)
        return Response({"message": "Got some data!", "data": request.data})
    print(request.GET)
    return Response({"message": "Hello, Howdy!"})