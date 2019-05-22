from Item.models import AccessToken, HookCalls, PullTransactions, Transaction
from Item.serializers import AccessTokenSerializer, TransactionSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from plaid_utils.Plaid import Client

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

class TransactionList(generics.ListAPIView):
    # """
    #     GET:
    #     Get List of transactions of a user
    # """

    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        user  = self.request.user
        return Transaction.objects.filter(user = user)



@api_view(['POST'])
@permission_classes((AllowAny, ))
def handleWebhook(request):
    print(request.data)
    hc = HookCalls(body=request.data)
    hc.save()
    if request.data["webhook_type"] == "TRANSACTIONS":
        try:
            item_id = request.data["item_id"]
            print(item_id)
            item = AccessToken.objects.get(itemid = item_id)
            print("Pulling Transaction")
            PullTransactions(item.a, item.user.id)
        except:
            print(Exception)
            pass
    return Response({"message": "Got some data!", "data": request.data})

@api_view(['POST'])
def fireWebhook(request):
    AT = AccessToken.objects.filter(user = request.user)
    fire_respose = []
    for at in AT:
        fr = Client.Sandbox.item.fire_webhook(at.a, 'DEFAULT_UPDATE')
        fire_respose.append(fr)
    return Response(fire_respose)
