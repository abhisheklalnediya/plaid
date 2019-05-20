from celery.decorators import task

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from plaid_utils.Plaid import Plaid


# Create your models here.

class AccessToken(models.Model) :
    a = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    plaid = Plaid()

    def setAccessToken(self, public_token):
       a = self.plaid.getAccessToken(public_token)
       return a


@receiver(post_save, sender=AccessToken, dispatch_uid="Start Pulling Details")
def PullDetails(sender, instance, **kwargs):
    print("Pull Details")