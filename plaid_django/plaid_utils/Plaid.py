import plaid
import os

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_PUBLIC_KEY = os.getenv('PLAID_PUBLIC_KEY')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions')



class Plaid():
    client = None
    user = None
    access_token = None

    def __init__(self):
        self.client = plaid.Client(client_id = PLAID_CLIENT_ID, secret=PLAID_SECRET, public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV, api_version='2018-05-22')
    
    def getAccessToken(self, public_token):
        try:
            exchange_response = self.client.Item.public_token.exchange(public_token)
        except plaid.errors.PlaidError as e:
            return e

        print(exchange_response)
        self.access_token = exchange_response['access_token']
        return self.access_token


