
from Item.models import AccessToken
from rest_framework import generics
from Item.serializers import AccessTokenSerializer
from Item.models import AccessToken

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
        print(self.request.data["public_token"])
        serializer.save(user=user)