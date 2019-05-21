import plaid
import os
from django.core.exceptions import SuspiciousOperation
from django.conf import settings


PLAID_CLIENT_ID = settings.PLAID_CLIENT_ID
PLAID_SECRET = settings.PLAID_SECRET
PLAID_PUBLIC_KEY = settings.PLAID_PUBLIC_KEY
PLAID_PRODUCTS = settings.PLAID_PRODUCTS
PLAID_ENV = settings.PLAID_ENV

Client = plaid.Client(client_id = PLAID_CLIENT_ID, secret=PLAID_SECRET, public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV, api_version='2018-05-22')

class Plaid():
    user = None
    access_token = None    
    
    def getAccessToken(self, public_token):
        try:
            exchange_response = Client.Item.public_token.exchange(public_token)
            print(exchange_response)
        except plaid.errors.PlaidError as e:
            raise SuspiciousOperation("Invalid public token")
        self.access_token = exchange_response['access_token']
        return self.access_token


