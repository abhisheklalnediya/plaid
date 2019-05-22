from Item.models import AccessToken, Transaction
from rest_framework import serializers

class AccessTokenSerializer(serializers.Serializer):
    public_token = serializers.CharField(max_length = 80)
    def create(self, validated_data):
        A = AccessToken(user = validated_data["user"])
        A.setAccessToken(validated_data["public_token"])
        A.save()
        return validated_data

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('date', 'amount', 'category')
