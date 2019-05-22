from celery.decorators import task
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.exceptions import SuspiciousOperation
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from plaid_utils.Plaid import Client, Plaid
from rest_framework.authtoken.models import Token

import datetime
import plaid


# Create your models here.

class AccessToken(models.Model):
    itemid = models.CharField(max_length=80, null=True, blank=True)
    a = models.CharField(max_length=80, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    plaid = Plaid()

    def setAccessToken(self, public_token):
       self.a = self.plaid.getAccessToken(public_token)
       return self.a


class Account(models.Model):
    account_id = models.CharField(max_length=80)
    balances = JSONField()
    mask = models.CharField(max_length=80, null=True, blank=True)
    name = models.CharField(max_length=80)
    official_name = models.TextField(null=True, blank=True)
    subtype = models.CharField(max_length=80, null=True, blank=True)
    type = models.CharField(max_length=80)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE )
    account_owner = models.CharField(max_length=80, null=True, blank=True)
    amount = models.IntegerField()
    category = ArrayField(models.CharField(max_length=80))
    category_id = models.CharField(max_length=80)
    date = models.DateField()
    iso_currency_code = models.CharField(max_length=5)
    location = JSONField()
    name = models.CharField(max_length=80)
    payment_meta = JSONField()
    pending = models.BooleanField()
    pending_transaction_id = models.CharField(max_length=80, null=True, blank=True)  # FK self??
    transaction_id = models.CharField(max_length=80)
    transaction_type = models.CharField(max_length=80)
    unofficial_currency_code  = models.CharField(max_length=80, null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=AccessToken, dispatch_uid="Start Pulling Details")
def PullDetails(sender, instance, **kwargs):
    PullIdentity.delay(instance.a, instance.user.id)


def insertAccounts(accounts_data, userid):
    user = User.objects.get(id = userid)
    for ad in accounts_data:
        a, created = Account.objects.get_or_create(
            user = user, account_id = ad["account_id"],
            defaults={
                "balances": ad["balances"],
                "mask": ad["mask"],
                "name": ad["name"],
                "official_name": ad["official_name"],
                "subtype": ad["subtype"],
                "type": ad["type"],
            },
        )


def insertTransactions(transaction_data, userid):
    user = User.objects.get(id = userid)
    for td in transaction_data:                     # Bad idea
        a, created = Transaction.objects.get_or_create(
            user = user, transaction_id = td["transaction_id"],
            defaults = {
                "account_id" : Account.objects.get(account_id = td["account_id"]),
                "account_owner" : td["account_owner"],
                "amount" : td["amount"],
                "category" : td["category"],
                "category_id" : td["category_id"],
                "date" : td["date"],
                "iso_currency_code" : td["iso_currency_code"],
                "location" : td["location"],
                "name" : td["name"],
                "payment_meta" : td["payment_meta"],
                "pending" : td["pending"],
                "pending_transaction_id" : td["pending_transaction_id"],
                "transaction_type" : td["transaction_type"],
                "unofficial_currency_code" : td["unofficial_currency_code"],
            },
        )


@task(name="pullTransactions")
def PullTransactions(access_token, userid):
    start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-30))
    end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
    try:
        transactions_response = Client.Transactions.get(access_token, start_date, end_date)
        insertAccounts(transactions_response["accounts"], userid)
        insertTransactions(transactions_response["transactions"], userid)
    except plaid.errors.PlaidError as e:
        raise SuspiciousOperation("Error")
    return None

@task(name="pullIdentity")
def PullIdentity(access_token, userid):
    s = ""
    try:
        s = Token.objects.get(user__id = userid).key[::-1]
    except:
        pass
    try:
        item_response = Client.Item.get(access_token)
        at = AccessToken.objects.get(a = access_token)
        at.itemid = item_response["item"]["item_id"]
        at.save()
        # subscribe to webhook
        Client.Item.webhook.update(access_token, settings.WEBHOOKEP + "?s" + s )

        # pull transactions once item details are there
        # PullTransactions.delay(access_token, userid)
    except plaid.errors.PlaidError as e:
        raise SuspiciousOperation("Error")
    return None

