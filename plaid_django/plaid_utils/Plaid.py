import plaid
import os
from django.core.exceptions import SuspiciousOperation

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_PUBLIC_KEY = os.getenv('PLAID_PUBLIC_KEY')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions')

PLAID_CLIENT_ID = "5cde2115736cca00137ef568"
PLAID_SECRET= "4aeb4e3abd4f2a523be49747589f75"
PLAID_PUBLIC_KEY= "2dc2351ad61dbf52196b0b94aaf3ed"
PLAID_PRODUCTS= "transactions  "
PLAID_ENV= "sandbox"
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


